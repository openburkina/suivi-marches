from django.db import models
from .abstract_models import Document
from .constants import TENDER_STATUS, PROCUREMENT_METHOD, AWARD_CRITERIA, SUBMISSION_METHOD

class Address(models.Model):
    country_name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    locality = models.CharField(max_length=255) # Town
    postal_code = models.CharField(max_length=255)

class ContactPoint(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    faxNumber = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    contact_point = models.ForeignKey(ContactPoint, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

class Value(models.Model):
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3)

class Tender(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
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
    award_period = models.ForeignKey(Period, on_delete=models.DO_NOTHING, related_name='award_period')


class TenderDocument(Document):
    tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING)

class Milestone(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    date_modified = models.CharField(max_length=255)
    status = models.CharField(max_length=255) #

class MilestoneDocument(Document):
    milestone = models.ForeignKey(Milestone, on_delete=models.DO_NOTHING)
