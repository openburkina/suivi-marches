import datetime

from django.db import models

from ocds_master_tables.models import Entity
from ocds_tender.models import Buyer, Tender
from ocds_awards.models import Award
from ocds_contracts.models import Contract
from ocds_planning.models import Planning

from .constants import INITIATION_TYPE, PARTY_ROLE, RELEASE_TAG_CHOICES

class Record(models.Model):
    ocid = models.CharField(max_length=255)
    compiled_release = models.OneToOneField('Release', on_delete=models.DO_NOTHING, null=True, blank=True)

    def save(self, *args, **kwargs):
        # update_or_create compîled_release
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.ocid)

class Release(models.Model):
    ref_record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    ocid = models.CharField(max_length=255, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=255, choices=RELEASE_TAG_CHOICES)
    initiation_type = models.CharField(max_length=255, default='tender', choices=INITIATION_TYPE)
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING, null=True, blank=True)
    planning = models.ForeignKey(Planning, on_delete=models.DO_NOTHING, null=True, blank=True)
    tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING, null=True, blank=True)

    def set_ocid(self, *args, **kwargs):
        inc = 1
        self.ocid = self.ref_record.ocid + '-' + str(inc) + '-' + self.tag
        while self.ref_record.release_set.filter(ocid=self.ocid):
            inc += 1

    def update_date(self, *args, **kwargs):
        self.date = datetime.datetime.now()

    def save(self, *args, **kwargs):
        self.set_ocid(self, *args, **kwargs)
        if self.pk:
            self.update_date(self, *args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.ocid)

class ReleaseAward(Award):
    ref_release = models.ForeignKey(Release, on_delete=models.DO_NOTHING)

class ReleaseContract(Contract):
    ref_release = models.ForeignKey(Release, on_delete=models.DO_NOTHING)

class ReleaseParty(Entity):
    ref_release = models.ForeignKey(Release, on_delete=models.DO_NOTHING)

class ReleasePartyRole(models.Model):
    name = models.CharField(max_length=255, choices=PARTY_ROLE)
    ref_release_party = models.ForeignKey(ReleaseParty, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)
