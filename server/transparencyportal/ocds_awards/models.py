from django.db import models
from ocds_master_tables.models import Amendment, Document, Entity, Item, Period, Value
from .constants import AWARD_STATUS

class Award(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=AWARD_STATUS)
    date = models.DateTimeField()
    value = models.OneToOneField(Value, on_delete=models.DO_NOTHING)
    contract_period = models.OneToOneField(Period, on_delete=models.DO_NOTHING)

class Supplier(Entity):
    ref_award = models.ForeignKey(Award, on_delete=models.DO_NOTHING)

class AwardItem(Item):
    ref_award = models.ForeignKey(Award, on_delete=models.DO_NOTHING)

class AwardDocument(Document):
    ref_award = models.ForeignKey(Award, on_delete=models.DO_NOTHING)

class AwardAmendment(Amendment):
    ref_award = models.OneToOneField(Award, on_delete=models.DO_NOTHING)
