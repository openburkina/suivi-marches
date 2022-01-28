from django.shortcuts import render
from django.db.models import F, Count

from rest_framework.views import APIView
from rest_framework.response import Response


import requests

from ocds_master_tables.serializers import RegionSerializer
from ocds_release.models import Record

from .constants import page_id_1, facebook_access_token_1
# Create your views here.

class RegionListView(APIView):
    def get(self, request):
        regions = Record.objects.values(
            'implementation_address__country_name',
            'implementation_address__region'
        ).annotate(
            number=Count('implementation_address__region')
            )
        data = RegionSerializer(regions, many=True).data
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