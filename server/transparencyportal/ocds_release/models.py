import datetime

from django.db import models
from django.db.models.deletion import PROTECT

from ocds_release.custom_fields import ChoiceArrayField
from ocds_master_tables.models import Entity, Address, Value
from ocds_awards.models import Award
from ocds_contracts.models import Contract
from ocds_planning.models import Planning

from .utils import to_json_publication
from .constants import INITIATION_TYPE, PARTY_ROLE, RELEASE_TAG_CHOICES

class Target(models.Model):
    name = models.CharField(max_length=255)

class Record(models.Model):
    ocid = models.CharField(max_length=255)
    target = models.ForeignKey(Target, on_delete=models.PROTECT, null=True)
    implementation_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)
    implementation_value = models.ForeignKey(Value, on_delete=models.PROTECT, null=True)

    def save(self, *args, **kwargs):
        # update_or_create compîled_release
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.ocid)

class PublishedRelease(models.Model):
    ref_record = models.ForeignKey(Record, related_name='releases', on_delete=models.DO_NOTHING)
    release = models.JSONField()

class Release(models.Model):
    ref_record = models.OneToOneField(Record, related_name='compiled_release', on_delete=models.DO_NOTHING, null=True, blank=True)
    ocid = models.CharField(max_length=255, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    tag = ChoiceArrayField(models.CharField(max_length=255, choices=RELEASE_TAG_CHOICES))
    initiation_type = models.CharField(max_length=255, default='tender', choices=INITIATION_TYPE)
    buyer = models.ForeignKey('ReleaseParty', related_name='releases', on_delete=models.DO_NOTHING, null=True, blank=True)
    planning = models.OneToOneField(Planning, on_delete=models.DO_NOTHING, null=True, blank=True)
    tender = models.OneToOneField('ocds_tender.Tender', on_delete=models.DO_NOTHING, null=True, blank=True)

    def set_ocid(self, *args, **kwargs):
        inc = self.ref_record.releases.count() + 1
        self.ocid = self.ref_record.ocid + '-' + str(inc) + '-' + str(self.date)

    def update_date(self, *args, **kwargs):
        self.date = datetime.datetime.now()

    def publish(self, *args, **kwargs):
        self_instance = Release.objects.get(pk=self.pk)
        publication = PublishedRelease.objects.create(ref_record=self.ref_record, release=to_json_publication(self_instance))
        publication.save()
        self.set_ocid()

    def save(self, *args, **kwargs):
        self.set_ocid(self, *args, **kwargs)
        if self.pk:
            self.update_date(self, *args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.ocid)

class ReleaseAward(Award):
    ref_release = models.ForeignKey(Release, related_name='awards', on_delete=models.DO_NOTHING)

class ReleaseContract(Contract):
    ref_release = models.ForeignKey(Release, related_name='contracts', on_delete=models.DO_NOTHING)

class ReleaseParty(Entity):
    ref_release = models.ForeignKey(Release, related_name='parties', on_delete=models.DO_NOTHING)
    role = ChoiceArrayField(models.CharField(max_length=255, choices=PARTY_ROLE), null=True)
