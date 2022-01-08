from django.shortcuts import render
from rest_framework import viewsets

from ocds_planning.models import Planning
from ocds_planning.serializers import PlanningSerializers

class PlanningViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializers
