from django.db import models
from ocds_master_tables.models import Document, Budget, Value

# Create your models here.


class Planning(models.Model):
    raison = models.TextField(null=True, blank=True)
    budget = models.OneToOneField(Budget, on_delete=models.DO_NOTHING, null=True, blank=True)

class PlanningDocument(Document):
    planning = models.ForeignKey(Planning, on_delete=models.DO_NOTHING)
