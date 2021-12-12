from django.db import models
from ocds_master_tables.models import Amendment, Document, Entity, Item, Milestone, Period, Value
from .constants import TENDER_STATUS, PROCUREMENT_METHOD, AWARD_CRITERIA, SUBMISSION_METHOD

class Buyer(Entity):
    pass

class Tender(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=TENDER_STATUS, null=True, blank=True)
    procurement_method = models.CharField(max_length=255, choices=PROCUREMENT_METHOD, null=True, blank=True)
    procurement_method_rationale = models.TextField(null=True, blank=True)
    award_criteria = models.CharField(max_length=255, choices=AWARD_CRITERIA, null=True, blank=True)
    award_criteria_details = models.TextField(null=True, blank=True)
    submission_method = models.CharField(max_length=255, choices=SUBMISSION_METHOD, null=True, blank=True)
    submission_method_details = models.TextField(null=True, blank=True)
    min_value = models.ForeignKey(Value, on_delete=models.DO_NOTHING, related_name='as_min_value_tenders', null=True, blank=True)
    value = models.ForeignKey(Value, on_delete=models.DO_NOTHING, related_name='as_default_value_tenders', null=True, blank=True)
    tender_period = models.ForeignKey(Period, on_delete=models.DO_NOTHING, related_name='as_tender_period_tenders', null=True, blank=True)
    enquiry_period = models.ForeignKey(Period, on_delete=models.DO_NOTHING, related_name='as_enquiry_period_tenders', null=True, blank=True)
    has_enquiries = models.BooleanField(default=False)
    eligibility_criteria = models.TextField(null=True, blank=True)
    award_period = models.ForeignKey(Period, on_delete=models.DO_NOTHING, related_name='as_award_period_tenders', null=True, blank=True)
    number_of_tenderers = models.PositiveIntegerField(null=True, blank=True)
    procuring_entity = models.ForeignKey(Entity, on_delete=models.DO_NOTHING, related_name='as_procuring_entity_tenders', null=True, blank=True)

    def __str__(self):
        return '%s - %s (%s)' % (self.id, self.title, self.status)

class TenderAmendment(Amendment):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)

class TenderItem(Item):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)

class TenderDocument(Document):
    tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING)

class TenderMilestone(Milestone):
    tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING)

class Tenderer(Entity):
    ref_tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING)
