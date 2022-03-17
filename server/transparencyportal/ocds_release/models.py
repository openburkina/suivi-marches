import datetime

from django.db import models

from ocds_release.custom_fields import ChoiceArrayField
from ocds_master_tables.models import Entity, Address, Value
from ocds_planning.models import Planning
from transparencyportal.api_doc import send

from .utils import to_json_publication
from .constants import INITIATION_TYPE, PARTY_ROLE, RELEASE_TAG_CHOICES

class Target(models.Model):
    name = models.CharField(max_length=255)

class Record(models.Model):
    ocid = models.CharField(max_length=255, unique=True)
    target = models.ForeignKey(Target, on_delete=models.PROTECT, null=True)
    implementation_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True)
    implementation_value = models.ForeignKey(Value, on_delete=models.PROTECT, null=True)

    def save(self,*args, **kwargs):
        send.FacebookPublishView(*args)
        # update_or_create compîled_release
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.ocid)

class PublishedRelease(models.Model):
    ref_record = models.ForeignKey(Record, related_name='releases', on_delete=models.DO_NOTHING)
    release = models.JSONField()

class Role(models.Model):
    release = models.ForeignKey('Release', on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    role = ChoiceArrayField(models.CharField(max_length=255, choices=PARTY_ROLE), null=True)

class Release(models.Model):
    ref_record = models.OneToOneField(Record, related_name='compiled_release', on_delete=models.DO_NOTHING, null=True, blank=True)
    ocid = models.CharField(max_length=255, editable=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    tag = ChoiceArrayField(models.CharField(max_length=255, choices=RELEASE_TAG_CHOICES))
    initiation_type = models.CharField(max_length=255, default='tender', choices=INITIATION_TYPE)
    buyer = models.ForeignKey(Entity, related_name='releases', on_delete=models.DO_NOTHING, null=True, blank=True)
    planning = models.OneToOneField(Planning, on_delete=models.DO_NOTHING, null=True, blank=True)
    tender = models.OneToOneField('ocds_tender.Tender', on_delete=models.DO_NOTHING, null=True, blank=True)
    parties = models.ManyToManyField(Entity, through='Role')


    @property
    def step(self):
        for (step, verbose) in reversed(RELEASE_TAG_CHOICES):
            if step in self.tag:
                return step

    @property
    def suppliers(self):
        return self.parties.filter(role__role__contains=['supplier']).values_list('name', flat=True)

    def add_role(self, party, role_name):
        role_instance, created = Role.objects.get_or_create(release=self, entity=party)
        if role_instance.role:
            role_instance.role.append(role_name)
        else:
            role_instance.role = [role_name]
        role_instance.save()

    def remove_role(self, party, role_name):
        role_instance, created = Role.objects.get_or_create(release=self, entity=party)
        if role_instance.role:
            role_instance.role.remove(role_name)
        else:
            role_instance.role = [role_name]
        role_instance.save()

    def update_buyer_role(self):
        last_instance = Release.objects.get(pk=self.pk)
        if getattr(last_instance, 'buyer'):
            self.remove_role(getattr(last_instance, 'buyer'), 'buyer')
        if getattr(self, 'buyer'):
            self.add_role(getattr(self, 'buyer'), 'buyer')

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
