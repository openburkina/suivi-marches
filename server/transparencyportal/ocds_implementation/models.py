from django.db import models
from ocds_master_tables.models import Document, Entity, Milestone, Organization, Value

class Implementation(models.Model):
    pass

class Transaction(models.Model):
    implementation = models.ForeignKey(Implementation, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.OneToOneField(Value, null=True, blank=True, on_delete=models.CASCADE)
    provider_organization = models.OneToOneField(Organization, related_name='provider_organization', null=True, blank=True, on_delete=models.DO_NOTHING)
    receiver_organization = models.OneToOneField(Organization, related_name='receiver_organization', null=True, blank=True, on_delete=models.DO_NOTHING)
    uri = models.CharField(max_length=255)

class ImplementationMilestone(Milestone):
    ref_implementation = models.ForeignKey(Implementation, on_delete=models.CASCADE)

class ImplementationDocument(Document):
    ref_implementation = models.ForeignKey(Implementation, on_delete=models.CASCADE)
