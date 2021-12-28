from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


import requests
from .constants import page_id_1, facebook_access_token_1
# Create your views here.

class FacebookPublishView(APIView):
    msg = 'Suivi des marchés publique Test d"API'
    payload = {
        'message': msg,
        'access_token': facebook_access_token_1
        }
    def post(self, request, post_url='https://graph.facebook.com/{}/feed'.format(page_id_1),data=payload ):
        r = requests.post(post_url, data)
        print(r.text)
        return Response(status=None)