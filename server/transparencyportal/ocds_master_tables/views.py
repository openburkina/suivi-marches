from django.shortcuts import get_object_or_404, render
from django.db.models import F, Count, Sum, Value
from django.db.models.functions import Concat

from rest_framework.views import APIView
from rest_framework.response import Response


import requests

from ocds_master_tables.serializers import RegionSerializer, RecordAggregateSerializer, RecordValueByGenericSerializer, RecordNumberByStatusYearSerializer, RecordValueBySectorYearSerializer, RecordValueEvolutionBySectorSerializer
from ocds_release.models import Record, Release
from ocds_master_tables.models import Address
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .constants import page_id_1, facebook_access_token_1
# Create your views here.

class RegionListView(APIView):
    @swagger_auto_schema(responses={200:RegionSerializer(many=True)})
    def get(self, request):
        regions = Record.objects.values(
            'implementation_address__country_name',
            'implementation_address__region'
        ).annotate(
            id = F('id'),
            number = Count('implementation_address__region')
            )
        data = RegionSerializer(regions, many=True).data
        return Response(data)

class RegionRecordListView(APIView):
    @swagger_auto_schema(responses={200:RecordAggregateSerializer(many=True)})
    def get(self, request, region_id):
        region_instance = get_object_or_404(Address, pk=region_id)
        releases = Release.objects.filter(
            ref_record__implementation_address = region_instance
        ).annotate(
                record_ocid = F('ref_record__ocid'),
                title = F('tender__title'),
                sector = F('ref_record__target__name'),
                buyer_name = F('buyer__name'),
                value = F('ref_record__implementation_value__amount'),
                currency = F('ref_record__implementation_value__currency'),
                last_update = F('date')
            )
        data = RecordAggregateSerializer(releases, many=True).data
        return Response(data)
 
class RegionRecordNumberByStatusYearView(APIView):
    @swagger_auto_schema(
        responses={200:RecordNumberByStatusYearSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, region_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        region_instance = get_object_or_404(Address, pk=region_id)
        releases = Release.objects.filter(
            ref_record__implementation_address = region_instance,
            date__year=year
        )
        output = {
            'planning': 0,
            'tender': 0,
            'award': 0,
            'contract': 0,
            'implementation': 0,
            'done': 0,
            'total': releases.count(),
        }
        for release in releases:
            output[release.step] += 1
        data = RecordNumberByStatusYearSerializer(output).data
        return Response(data)
 
class RegionRecordValueEvolutionBySectorView(APIView):
    @swagger_auto_schema(
        responses={200:RecordValueEvolutionBySectorSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('start_year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('end_year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
        ]
    )
    def get(self, request, region_id):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        if start_year is None or end_year is None:
            return Response('Year not specified', status=500)
        if int(start_year) > int(end_year):
            return Response('Start year is after end year', status=500)

        region_instance = get_object_or_404(Address, pk=region_id)
        records = Record.objects.filter(
            implementation_address=region_instance,
            compiled_release__date__year__gte=start_year,
            compiled_release__date__year__lte=end_year,
        ).values('compiled_release__date__year', sector=F('target__name'))\
            .annotate(value=Sum('implementation_value__amount'), currency=F('implementation_value__currency'))
        data = RecordValueEvolutionBySectorSerializer(records, many=True).data
        return Response(data)
 
class RegionRecordValueByGenericView(APIView):
    @swagger_auto_schema(
        responses={200:RecordValueByGenericSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('group_by', openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=['buyer', 'sector'], required=True)
        ]
    )
    def get(self, request, region_id):
        year = self.request.query_params.get('year')
        group_by = self.request.query_params.get('group_by')
        if year is None:
            return Response('Year not specified', status=500)
        if not group_by in ['buyer', 'sector']:
            return Response('Group field not specified', status=500)

        region_instance = get_object_or_404(Address, pk=region_id)
        records = Record.objects.filter(
                implementation_address=region_instance,
                compiled_release__date__year=year
            )
        if group_by == 'buyer':
            records = records.annotate(
                name=F('compiled_release__buyer__name')
            ).values('name')
        if group_by == 'sector':
            records = records.annotate(name=F('target__name')).values('name')
        records = records.annotate(value=Sum('implementation_value__amount'), currency=F('implementation_value__currency'))
        data = RecordValueByGenericSerializer(records, many=True).data
        return Response(data)
 
class FacebookPublishView(APIView):
    msg = "Ceci est un message test pour la publication des informations d'un marché publics"
    payload = {
        'message': msg,
        'access_token': facebook_access_token_1
        }
    def post(self, request, post_url='https://graph.facebook.com/{}/feed'.format(page_id_1),data=payload ):
        r = requests.post(post_url, data)
        print(r.text)
        return Response(status=None)