import json

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status

from ocds_release.models import Record, Release, PublishedRelease
from ocds_release.serializers import RecordSerializer, ReleaseSerializer, RecordStageSerializer, RecordItemSerializer
from ocds_tender.models import Buyer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class PublishedReleaseView(APIView):
    def get(self, request, pk):
        published_release_instance = get_object_or_404(PublishedRelease, pk=pk)
        return Response(json.loads(published_release_instance.release))

class RecordItemList(APIView):
    def get(self, request, record_id):
        record_instance = get_object_or_404(Record, pk=record_id)
        output_instance = {
            'id': record_instance.pk,
            'tender': '',
            'items': []
        }
        if record_instance.compiled_release is None:
            return Response(data=output_instance, status=status.HTTP_501_NOT_IMPLEMENTED)
        if record_instance.compiled_release.tender is None:
            return Response(data=output_instance, status=status.HTTP_501_NOT_IMPLEMENTED)
        output_instance['tender'] = record_instance.compiled_release.tender
        output_instance['items'] = record_instance.compiled_release.tender.items.all()
        data = RecordItemSerializer(output_instance, context={'request': request}).data
        return Response(data)

class RecordStageList(APIView):
    def get(self, request, record_id):
        record_instance = get_object_or_404(Record, pk=record_id)
        output_instance = {
            'id': record_instance.pk,
            'tender_period': {},
            'award_period': {},
            'awards': [],
        }
        if record_instance.compiled_release is None:
            return Response(data=output_instance, status=status.HTTP_501_NOT_IMPLEMENTED)
        if record_instance.compiled_release.tender is None:
            return Response(data=output_instance, status=status.HTTP_501_NOT_IMPLEMENTED)
        output_instance['tender_period'] = record_instance.compiled_release.tender.tender_period
        output_instance['award_period'] = record_instance.compiled_release.tender.award_period
        output_instance['awards'] = record_instance.compiled_release.awards.all()
        data = RecordStageSerializer(output_instance).data
        return Response(data)

class InProgressRecordList(APIView):
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Buyer, pk=buyer_id)
        queryset = Record.objects.filter(compiled_release__buyer = buyer_instance.pk).exclude(compiled_release__tag__contains = ['contractTermination'])
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class DoneRecordList(APIView):
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Buyer, pk=buyer_id)
        queryset = Record.objects.filter(
            compiled_release__buyer = buyer_instance.pk,
            compiled_release__tag__contains = ['contractTermination']
        )
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)
