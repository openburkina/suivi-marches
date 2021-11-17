from django.db import models
from ocds_master_tables.models import Amendment, Document, Entity, Item, Milestone, Period, Value
from .constants import TENDER_STATUS, PROCUREMENT_METHOD, AWARD_CRITERIA, SUBMISSION_METHOD

class Tender(models.Model):
    buyer = models.ForeignKey(Entity, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=TENDER_STATUS)
    procurement_method = models.CharField(max_length=255, choices=PROCUREMENT_METHOD)
    procurement_method_rationale = models.TextField()
    award_criteria = models.CharField(max_length=255, choices=AWARD_CRITERIA)
    award_criteria_details = models.TextField()
    submission_method = models.CharField(max_length=255, choices=SUBMISSION_METHOD)
    submission_method_details = models.TextField()
    min_value = models.ForeignKey(Value, on_delete=models.DO_NOTHING, related_name='min_value')
    value = models.ForeignKey(Value, on_delete=models.DO_NOTHING, related_name='default_value')
    tender_period = models.ForeignKey(Period, on_delete=models.DO_NOTHING, related_name='tender_period')
    enquiry_period = models.ForeignKey(Period, on_delete=models.DO_NOTHING, related_name='enquiry_period')
    has_enquiries = models.BooleanField(default=False)
    eligibility_criteria = models.TextField()
    award_period = models.ForeignKey(Period, on_delete=models.DO_NOTHING, related_name='award_period')
    number_of_tenderers = models.PositiveIntegerField()
    tenderer = models.OneToOneField(Entity, on_delete=models.DO_NOTHING, related_name='tenderer')
    procuring_entity = models.OneToOneField(Entity, on_delete=models.DO_NOTHING, related_name='procuring_entity')
    amendment = models.OneToOneField(Amendment, on_delete=models.DO_NOTHING)

class TenderItem(Item):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)

class TenderDocument(Document):
    tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING)

class TenderMilestone(Milestone):
    tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING)

class MilestoneDocument(Document):
    milestone = models.ForeignKey(TenderMilestone, on_delete=models.DO_NOTHING)
