from django.db import models
from ocds_master_tables.models import Amendment, Document, Entity, Item, Period, Value
from .constants import AWARD_STATUS

class Award(models.Model):
    release = models.ForeignKey('ocds_release.Release', related_name='awards', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=AWARD_STATUS, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    value = models.OneToOneField(Value, on_delete=models.DO_NOTHING, null=True, blank=True)
    contract_period = models.OneToOneField(Period, on_delete=models.DO_NOTHING, null=True, blank=True)
    suppliers = models.ManyToManyField(Entity, related_name='as_supplier_awards')

    def __str__(self):
        return '%s - %s' % (self.id, self.title)

class AwardItem(Item):
    ref_award = models.ForeignKey(Award, related_name='items', on_delete=models.DO_NOTHING)

class AwardDocument(Document):
    ref_award = models.ForeignKey(Award, related_name='documents', on_delete=models.DO_NOTHING)

class AwardAmendment(Amendment):
    ref_award = models.ForeignKey(Award, related_name='amendments', on_delete=models.DO_NOTHING)
