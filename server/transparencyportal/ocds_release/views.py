import json

from django.shortcuts import get_object_or_404

from ocds_master_tables.models import Entity
from ocds_master_tables.serializers import EntitySerializer
from ocds_release.models import PublishedRelease, Record, Release, Target
from ocds_release.serializers import (
    RecordByTargetSerializer,
    RecordItemSerializer,
    RecordSerializer,
    RecordStageSerializer,
    RecordSumSerializer,
    ReleaseSerializer,
    TargetSerializer,
)
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

class BuyerList(APIView):
    def get(self, request):
        buyers = Entity.objects.filter(role__name__contains=["buyer"])
        data = EntitySerializer(buyers, many=True).data
        return Response(data)

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

class RecordByTarget(APIView):
    def get(self, request, target_name):
        country = self.request.query_params.get('country')
        region = self.request.query_params.get('region')
        records = Record.objects.filter(target__name=target_name)
        if country:
            records = records.filter(implementation_address__country_name__iexact=country)
        if region:
            records = records.filter(implementation_address__region__iexact=region)
        output_instance = {
            'records' : records
        }
        data = RecordByTargetSerializer(output_instance, context={'request': request}).data
        return Response(data)

class InProgressRecordList(APIView):
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        queryset = Record.objects.filter(compiled_release__buyer = buyer_instance.pk).exclude(compiled_release__tag__contains = ['contractTermination'])
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class DoneRecordList(APIView):
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        queryset = Record.objects.filter(
            compiled_release__buyer = buyer_instance.pk,
            compiled_release__tag__contains = ['contractTermination']
        )
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class SumRecord(APIView):
    def post(self, request, region_id):
        queryset = Record.objects.filter(
            implementation_address__region__iexact = region_id
        )
        data = RecordSumSerializer(queryset, many=True, context={'request': request}).data
        return Response({
            'entity': data
        })
