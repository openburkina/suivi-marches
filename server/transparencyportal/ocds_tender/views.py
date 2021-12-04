from django.db.models import Q, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


from . import models
from . import serializers


class TenderViews(viewsets.ModelViewSet):
    queryset = models.Tender.objects.all()
    serializer_class = serializers.TenderSerializer

class TenderByAdress(APIView):
    def get(self, request, table=models.Tender, serializers_class=serializers.RatingSerializer,
             buyer_id=None):
        #entity = table.objects.raw('select 1 id, count(*) as total from ocds_tender_Tender T')
        entity = table.objects.raw('select 1 id, count(*) as total, A.region as "region_name" from ocds_tender_Tender T, ocds_master_tables_Entity E, ocds_master_tables_Address A WHERE E.id=%s AND E.id=A.id Group By A.region',[buyer_id])
        serializer = serializers_class(entity, many=True)
        return Response({
            'entities': serializer.data,
        })