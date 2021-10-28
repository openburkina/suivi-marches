from django.db import models
from master_tables.models import Organisation, OperatingUnit

class Offer(models.Model):
    """
    STATUS_TYPES
    0 : non assigné
    1 : en cours
    2 : terminé
    """
    id = models.CharField(max_length=100, db_index=True, primary_key=True)
    title = models.TextField(blank=True, null=True)
    organisation = models.ForeignKey(Organisation, related_name='organisation', blank=True, null=True, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=600, blank=True, null=True)
    contact_email = models.CharField(max_length=100, default=None, blank=True, null=True)
    contact_website = models.CharField(max_length=100, default=None, blank=True, null=True)
    operating_unit = models.ForeignKey(OperatingUnit, default=None, blank=True, null=True, db_index=True, on_delete=models.DO_NOTHING)
    status = models.IntegerField(blank=True, null=True)
    budget = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.id

class OfferDate(models.Model):
    """
    OFFER_STAGE_TYPES
    0 : non assigné
    1 : appel d'offre
    2 : début
    3 : reception
    4 : résultat
    5 : avenant
    6 : fin
    """
    id = models.CharField(max_length=100, db_index=True, primary_key=True)
    date = models.DateField(blank=True, null=True)
    stage_type = models.IntegerField(default=0)
    related_offer = models.ForeignKey(Offer, on_delete=models.DO_NOTHING)

class Lessor(models.Model):
    """
    Bailleur

    LESSOR_TYPES
    0 : inconnu
    1 : ministere
    2 : collectivité locale
    3 : organisme international
    """
    id = models.CharField(max_length=100, db_index=True, primary_key=True)
    title = models.TextField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    agreement = models.ManyToManyField(to=Offer, through='OfferAgreement')

class OfferAgreement(models.Model):
    id = models.CharField(max_length=100, db_index=True, primary_key=True)
    lessor = models.ForeignKey(Lessor, on_delete=models.DO_NOTHING)
    offer = models.ForeignKey(Offer, on_delete=models.DO_NOTHING)

class Disbursment(models.Model):
    """
    Décaissement
    """
    id = models.CharField(max_length=100, db_index=True, primary_key=True)
    value = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    offer_agreement = models.ForeignKey(OfferAgreement, on_delete=models.DO_NOTHING)
