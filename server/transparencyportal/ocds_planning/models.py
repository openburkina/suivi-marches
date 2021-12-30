from django.db import models
from ocds_master_tables.models import Document, Budget, Milestone, Value

class Planning(models.Model):
    raison = models.TextField(null=True, blank=True)
    budget = models.OneToOneField(Budget, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.budget)

class PlanningDocument(Document):
    planning = models.ForeignKey(Planning, related_name='documents', on_delete=models.DO_NOTHING)

class PlanningMilestone(Milestone):
    planning = models.ForeignKey(Planning, related_name='milestones', on_delete=models.DO_NOTHING)
