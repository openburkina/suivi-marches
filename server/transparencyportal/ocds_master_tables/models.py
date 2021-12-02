from django.db import models
from .constants import CLASSIFICATION_SCHEME, DOCUMENT_TYPE, MILESTONE_STATUS

class Address(models.Model):
    country_name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    locality = models.CharField(max_length=255) # Town
    postal_code = models.CharField(max_length=255)

    def __str__(self):
        return '%s, %s' % (self.locality, self.country_name)

class Amendment(models.Model):
    date = models.DateTimeField()
    rationale = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.id, self.date)

class Change(models.Model):
    amendment = models.ForeignKey(Amendment, on_delete=models.CASCADE)
    property = models.CharField(max_length=255)
    former_value = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.property)

class Classification(models.Model):
    scheme = models.CharField(max_length=255, choices=CLASSIFICATION_SCHEME)
    description = models.TextField()
    uri = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.id, self.scheme)

class ContactPoint(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    faxNumber = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)

class Document(models.Model):

    class Meta:
        abstract = True

    document_type = models.CharField(max_length=255, choices=DOCUMENT_TYPE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()
    document_format = models.CharField(max_length=255) # with choices
    language = models.CharField(max_length=255) # with choices

    def __str__(self):
        return '%s - %s (%s)' % (self.id, self.title, self.document_type)

class Entity(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.OneToOneField('Identifier', on_delete=models.DO_NOTHING)
    address = models.OneToOneField('Address', on_delete=models.DO_NOTHING)
    contact_point = models.OneToOneField('ContactPoint', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)

class Identifier(models.Model):
    scheme = models.CharField(max_length=255) # with choices
    legal_name = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.id, self.legal_name)

class EntityAdditionalIdentifier(Identifier):
    ref_entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

class Item(models.Model):
    description = models.TextField()
    classification = models.OneToOneField(Classification, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.IntegerField()
    unit = models.OneToOneField('Unit', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return '%s - %s %s' % (self.id, self.quantity, self.unit.name)

class ItemAdditionalClassification(Classification):
    ref_item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Milestone(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    date_modified = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=MILESTONE_STATUS)

    def __str__(self):
        return '%s - %s' % (self.id, self.title)

class MilestoneDocument(Document):
    ref_milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)

class Organization(models.Model):
    scheme = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.id, self.legal_name)

class Period(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s : %s' % (str(self.start_date), str(self.end_date))

class Unit(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    value = models.OneToOneField('Value', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.value)

class Value(models.Model):
    amount = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return '%s %s' % (self.amount, self.currency)

class Projet(models.Model):
    titre_projet = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.id, self.titre_projet)

class Budget(models.Model):
    source = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.ForeignKey(Value, on_delete=models.DO_NOTHING, null=True, blank=True)
    projet = models.ForeignKey(Projet, on_delete=models.DO_NOTHING, null=True, blank=True)
    uri = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s - %s (%s)' % (self.id, self.source, str(self.amount))