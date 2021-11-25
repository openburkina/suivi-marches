from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from ocds_release.models import Record
from .serializers import RecordSerializer
from ocds_master_tables.models import Entity

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class InProgressRecordList(APIView):
    def get(self, request, buyer_id):
        queryset = Record.objects.filter(compiled_release__buyer = buyer_id).exclude(compiled_release__tag = 'contractTermination')
        data = RecordSerializer(queryset, many=True).data
        return Response(data)

class DoneRecordList(APIView):
    def get(self, request, buyer_id):
        queryset = Record.objects.filter(
            compiled_release__buyer = buyer_id,
            compiled_release__tag = 'contractTermination'
        )
        data = RecordSerializer(queryset, many=True).data
        return Response(data)
