from django.contrib import admin
from undp_public_market.models import Lessor, Offer, OfferDate, OfferAgreement, Disbursment

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass

@admin.register(OfferDate)
class OfferDateAdmin(admin.ModelAdmin):
    pass

@admin.register(OfferAgreement)
class OfferAgreementAdmin(admin.ModelAdmin):
    pass

@admin.register(Disbursment)
class DisbursmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Lessor)
class LessorAdmin(admin.ModelAdmin):
    pass
