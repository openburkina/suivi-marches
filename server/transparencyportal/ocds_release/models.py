from django.db import models

from ocds_master_tables.models import Entity
from ocds_tender.models import Tender
from ocds_awards.models import Award
from ocds_contracts.models import Contract
from ocds_planning.models import Planning

from .constants import INITIATION_TYPE, PARTY_ROLE, RELEASE_TAG_CHOICES

class Record(models.Model):
    compiled_release = models.OneToOneField('Release', on_delete=models.DO_NOTHING, null=True, blank=True)

class Release(models.Model):
    ref_record = models.ForeignKey(Record, on_delete=models.DO_NOTHING, null=True, blank=True)
    ocid = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    tag = models.CharField(max_length=255, choices=RELEASE_TAG_CHOICES)
    initiation_type = models.CharField(max_length=255, default='tender', choices=INITIATION_TYPE)
    buyer = models.ForeignKey(Entity, on_delete=models.DO_NOTHING, null=True, blank=True)
    planning = models.OneToOneField(Planning, on_delete=models.DO_NOTHING, null=True, blank=True)
    tender = models.OneToOneField(Tender, on_delete=models.DO_NOTHING, null=True, blank=True)

class ReleaseAward(Award):
    ref_release = models.ForeignKey(Release, on_delete=models.DO_NOTHING)

class ReleaseContract(Contract):
    ref_release = models.ForeignKey(Release, on_delete=models.DO_NOTHING)

class ReleaseParty(Entity):
    ref_release = models.ForeignKey(Release, on_delete=models.DO_NOTHING)

class ReleasePartyRole(models.Model):
    name = models.CharField(max_length=255, choices=PARTY_ROLE)
    ref_release_party = models.ForeignKey(ReleaseParty, on_delete=models.CASCADE)
