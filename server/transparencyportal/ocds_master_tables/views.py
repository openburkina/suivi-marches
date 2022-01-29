from django.shortcuts import get_object_or_404, render
from django.db.models import F, Count

from rest_framework.views import APIView
from rest_framework.response import Response


import requests

from ocds_master_tables.serializers import RegionSerializer, RecordAggregateSerializer, RecordValueByGenericSerializer, RecordNumberByStatusYearSerializer, RecordValueBySectorYearSerializer, RecordValueEvolutionBySectorSerializer
from ocds_release.models import Record, Release
from ocds_master_tables.models import Address

from .constants import page_id_1, facebook_access_token_1
# Create your views here.

class RegionListView(APIView):
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