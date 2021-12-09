from django.shortcuts import render
from rest_framework import viewsets

from ocds_planning.models import Planning
from ocds_planning.serializers import PlanningSerializers

class PlanningViewSet(viewsets.ModelViewSet):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializers
