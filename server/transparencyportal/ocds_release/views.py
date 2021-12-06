import datetime

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from ocds_release.models import Record, Release
from ocds_release.serializers import RecordSerializer, ReleaseSerializer, RecordStageSerializer, RecordItemSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class RecordItemList(APIView):
    def get(self, request, record_id):
        record_instance = Record.objects.get(pk=record_id)
        output_instance = {
            'id': record_instance.pk,
            'tender': record_instance.compiled_release.tender,
            'items': record_instance.compiled_release.tender.tenderitem_set.all()
        }
        data = RecordItemSerializer(output_instance, context={'request': request}).data
        return Response(data)

class RecordStageList(APIView):
    def get(self, request, record_id):
        record_instance = Record.objects.get(pk=record_id)
        award_set = record_instance.compiled_release.tender.award_set.all()
        output_instance = {
            'id': record_instance.pk,
            'tender_period': record_instance.compiled_release.tender.tender_period,
            'award_period': record_instance.compiled_release.tender.award_period,
            'awards': award_set,
        }
        data = RecordStageSerializer(output_instance).data
        return Response(data)

class InProgressRecordList(APIView):
    def get(self, request, buyer_id):
        queryset = Record.objects.filter(compiled_release__buyer = buyer_id).exclude(compiled_release__tag = 'contractTermination')
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class DoneRecordList(APIView):
    def get(self, request, buyer_id):
        queryset = Record.objects.filter(
            compiled_release__buyer = buyer_id,
            compiled_release__tag = 'contractTermination'
        )
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)
