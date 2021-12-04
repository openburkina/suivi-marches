from django.db.models import Q, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


from ocds_tender.models import Buyer, Tender
from ocds_tender.serializers import BuyerSerializer, TenderSerializer


class TenderViews(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

class TenderByAdress(APIView):
    def get(self, request, table=models.Tender, serializers_class=serializers.RatingSerializer,
             buyer_id=None):
        #entity = table.objects.raw('select 1 id, count(*) as total from ocds_tender_Tender T')
        entity = table.objects.raw('select 1 id, count(*) as total, A.region as "region_name" from ocds_tender_Tender T, ocds_master_tables_Entity E, ocds_master_tables_Address A WHERE T.buyer=%s AND E.address=A.id Group By A.region',[buyer_id])
        serializer = serializers_class(entity, many=True)
        return Response({
            'entities': serializer.data,
        })
class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
