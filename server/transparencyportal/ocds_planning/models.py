from django.db import models
from ocds_master_tables.models import Document, Budget, Value

# Create your models here.


class Planning(models.Model):
    raison = models.TextField()
    budget = models.ForeignKey(Budget, on_delete=models.DO_NOTHING)
    amount = models.ForeignKey(Value, on_delete=models.DO_NOTHING)


class PlanningDocument(Document):
    planning = models.ForeignKey(Planning, on_delete=models.DO_NOTHING)
