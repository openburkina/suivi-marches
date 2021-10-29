from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from master_tables.models import Organisation, OperatingUnit



from . import models
from . import serializers
from .serializers import OfferListingField, LessorListingField,OfferField, OfferDateListingField, OfferAgreementListingField, DisbursmentListingField


class ViewsetOffer(viewsets.ModelViewSet):
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferListingField


class ViewsetLessor(viewsets.ModelViewSet):
    queryset = models.Lessor.objects.all()
    serializer_class = serializers.LessorListingField


class ViewsetOfferDate(viewsets.ModelViewSet):
    queryset = models.OfferDate.objects.all()
    serializer_class = serializers.OfferDateListingField


class ViewsetDisbursment(viewsets.ModelViewSet):
    queryset = models.Disbursment.objects.all()
    serializer_class = serializers.DisbursmentListingField


class OfferList(generics.ListAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OfferField
    filter_backends = [DjangoFilterBackend]
    #filters_fields = ['status']