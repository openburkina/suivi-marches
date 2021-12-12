from django.db import models
from .constants import CONTRACT_STATUS
from ocds_master_tables.models import Amendment, Document, Item, Milestone, Period, Value
from ocds_awards.models import Award

class Contract(models.Model):
    ref_award = models.OneToOneField(Award, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=CONTRACT_STATUS)
    period = models.OneToOneField(Period, null=True, blank=True, on_delete=models.DO_NOTHING)
    date_signed = models.DateTimeField(null=True, blank=True)
    value = models.OneToOneField(Value, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.id, self.title)

class ContractAmendment(Amendment):
    ref_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

class ContractItem(Item):
    ref_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

class ContractDocument(Document):
    ref_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

class ContractMilestone(Milestone):
    ref_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
