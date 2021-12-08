from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


from ocds_tender.models import Buyer, Tender
from ocds_tender.serializers import BuyerSerializer, TenderSerializer, RatingSerializer


class TenderViews(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

class TenderByAdress(APIView):
    def get(self, request, table=Tender, serializers_class=RatingSerializer,
             buyer_id=None):
        entity = table.objects.raw('select 1 id, count(T) as total, A.region as "region_name" from ocds_tender_Tender T, ocds_master_tables_Entity E, ocds_master_tables_Address A WHERE T.buyer_id=%s AND T.procuring_entity_id = E.address_id AND E.address_id=A.id Group By A.region order by total desc',[buyer_id])
        serializer = serializers_class(entity, many=True)
        return Response({
            'entities': serializer.data,
        })
class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
