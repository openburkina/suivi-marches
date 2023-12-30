from django.db import models
from ocds_master_tables.models import Document, Entity, Milestone, Value
from ocds_contracts.models import Contract

class Implementation(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.contract)

class Transaction(models.Model):
    implementation = models.ForeignKey(Implementation, related_name='transactions', on_delete=models.CASCADE, null=True, blank=True)
    source = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    value = models.OneToOneField(Value, null=True, blank=True, on_delete=models.CASCADE)
    payer = models.ForeignKey(Entity, related_name='as_payer_transactions', null=True, blank=True, on_delete=models.DO_NOTHING)
    payee = models.ForeignKey(Entity, related_name='as_payee_transactions', null=True, blank=True, on_delete=models.DO_NOTHING)
    uri = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s - %s : %s %s' % (self.payer.name, self.payee.name, str(self.value.amount), self.value.currency)

class ImplementationMilestone(Milestone):
    ref_implementation = models.ForeignKey(Implementation, related_name='milestones', on_delete=models.CASCADE)

class ImplementationDocument(Document):
    ref_implementation = models.ForeignKey(Implementation, related_name='documents', on_delete=models.CASCADE)
