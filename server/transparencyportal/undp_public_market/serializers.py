from rest_framework import serializers
from .models import Offer, OfferDate, Lessor, OfferAgreement, Disbursment
from master_tables.models import Organisation, OperatingUnit


# OfferDate Serializer
class OfferDateListingField(serializers.ModelSerializer):
    class Meta:
        model = OfferDate
        fields = '__all__'


# Offer Serializer
class OfferListingField(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


# Lessor Serializer
class LessorListingField(serializers.ModelSerializer):
    class Meta:
        model = Lessor
        fields = '__all__'


# OfferAgreement Serializer
class OfferAgreementListingField(serializers.ModelSerializer):
    class Meta:
        model = OfferAgreement
        fields = '__all__'


# Disbursment Serializer
class DisbursmentListingField(serializers.ModelSerializer):
    class Meta:
        model = Disbursment
        fields = '__all__'


# Offer Serializer
class OfferField(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = (
                    'id',
                    'title',
                    'organisation',
                    'description',
                    'contact_email',
                    'contact_website',
                    'operating_unit',
                    'status',
                    'budget',
                )