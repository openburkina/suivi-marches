from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date, datetime
from rest_framework import status



from ocds_tender.models import Buyer, Tender
from ocds_tender.serializers import BuyerSerializer, TenderSerializer, RatingSerializer, TenderStateMount


class TenderViews(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

class TenderByAdress(APIView):
    def get(self, request, table=Tender, serializers_class=RatingSerializer,
             buyer_id=None):
        buyer_instance = get_object_or_404(Buyer, pk=buyer_id)
        entity = table.objects.raw('select 1 id, count(T) as total, A.region as "region_name" from ocds_tender_Tender T, ocds_master_tables_Entity E, ocds_master_tables_Address A WHERE T.buyer_id=%s AND T.procuring_entity_id = E.address_id AND E.address_id=A.id Group By A.region order by total desc',[buyer_id])
        serializer = serializers_class(entity, many=True)
        return Response({
            'entities': serializer.data,
        })
class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class TenderStateAndMount(APIView):
    def post(self, request,year_val=None):
        if len(year_val) < 4:
            print("Date error")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        sting_date_deb = year_val+'-01-01'
        string_date_fin = year_val+'-12-31'
       # now_deb = date(*map(int,sting_date_deb.split('-')))
        now_deb = datetime.strptime(sting_date_deb,'%Y-%m-%d').date()
       # now_fin = date(*map(int,string_date_fin.split('-')))
        now_fin = datetime.strptime(string_date_fin,'%Y-%m-%d').date()
        entity = Tender.objects.filter(tender_period__start_date__range=(now_deb,now_fin))
        serializer = TenderStateMount(entity, many= True)
        return Response({
            'entities': serializer.data
        })


