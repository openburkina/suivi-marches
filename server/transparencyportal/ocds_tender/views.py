from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


from . import models
from . import serializers


class TenderViews(viewsets.ModelViewSet):
    queryset = models.Tender.objects.all()
    serializer_class = serializers.TenderSerializer

