from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend


from . import models
from . import serializers
from .serializers import OfferListingField, LessorListingField, OfferDateListingField, OfferAgreementListingField, DisbursmentListingField


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
    queryset = models.Offer.objects.all()
    serializer_class = LessorListingField
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']