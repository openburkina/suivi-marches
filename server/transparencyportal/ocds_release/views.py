import json
from locale import currency
from django.db.models.aggregates import Sum
from django.db.models.expressions import F, Value
from django.db.models.functions import Concat, TruncYear
from django.db.models import Q, Subquery, OuterRef, ExpressionWrapper, ManyToManyField

from django.shortcuts import get_object_or_404

from ocds_implementation.serializers import TransactionSerializer
from ocds_master_tables.models import Entity, Value as Amount
from ocds_master_tables.serializers import EntitySerializer
from ocds_release.models import PublishedRelease, Record, Release, Role, Target
from ocds_release.serializers import (
    BuyerRecordByStatusSerializer,
    BuyerRecordSerializer,
    BuyerTotalRecordSerializer,
    RecordValueGroupedSerializer,
    RecordItemSerializer,
    RecordSectorGroupedSerializer,
    RecordSerializer,
    RecordStageSerializer,
    RecordSumSerializer,
    ReleaseSerializer,
    TargetSerializer,
    BuyerRecordTotalSerializer
)
from ocds_master_tables.serializers import (
    RecordValueByGenericSerializer,
    RecordNumberByStatusYearSerializer,
    RecordValueBySectorYearSerializer,
    RecordValueEvolutionBySectorSerializer,
    ItemSerializer
)
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# class RecordViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Record.objects.all()
#     serializer_class = RecordSerializer

#     def get_queryset(self):
#         queryset = Record.objects.all()
#         country = self.request.query_params.get('country')
#         region = self.request.query_params.get('region')
#         target = self.request.query_params.get('target')
#         if country is not None:
#             queryset = queryset.filter(implementation_address__country_name__iexact=country)
#         if region is not None:
#             queryset = queryset.filter(implementation_address__region__iexact=region)
#         if target is not None:
#             queryset = queryset.filter(target__name__iexact=target)
#         return queryset

#     @swagger_auto_schema(manual_parameters=[
#         openapi.Parameter('country', openapi.IN_QUERY, type=openapi.TYPE_STRING),
#         openapi.Parameter('region', openapi.IN_QUERY, type=openapi.TYPE_STRING),
#         openapi.Parameter('target', openapi.IN_QUERY, type=openapi.TYPE_STRING),
#     ])
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)


class ReleaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class TargetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer


class BuyerList(APIView):
    @swagger_auto_schema(responses={200: EntitySerializer(many=True)})
    def get(self, request):
        buyers = Entity.objects.filter(role__role__contains=["buyer"]).distinct()
        data = EntitySerializer(buyers, many=True).data
        return Response(data)


class BuyerTotalRecordView(APIView):
    @swagger_auto_schema(responses={200: BuyerTotalRecordSerializer})
    def get(self, request, buyer_id):
        buyers = Entity.objects.filter(role__role__contains=["buyer"])
        buyer_instance = get_object_or_404(buyers, pk=buyer_id)
        output_instance = {
            'in_progress': [],
            'done': [],
            'total': []
        }
        in_progress_sum = Record.objects \
            .filter(compiled_release__buyer=buyer_instance.pk) \
            .exclude(compiled_release__tag__contains=['contractTermination']) \
            .annotate(currency=F('implementation_value__currency')) \
            .values('currency') \
            .annotate(amount=Sum('implementation_value__amount'))
        done_sum = Record.objects \
            .filter(compiled_release__buyer=buyer_instance.pk) \
            .filter(compiled_release__tag__contains=['contractTermination']) \
            .annotate(currency=F('implementation_value__currency')) \
            .values('currency') \
            .annotate(amount=Sum('implementation_value__amount'))
        total = Record.objects \
            .filter(compiled_release__buyer=buyer_instance.pk) \
            .annotate(currency=F('implementation_value__currency')) \
            .values('currency') \
            .annotate(amount=Sum('implementation_value__amount'))
        output_instance['in_progress'] = in_progress_sum
        output_instance['done'] = done_sum
        output_instance['total'] = total
        data = BuyerTotalRecordSerializer(output_instance).data
        return Response(data)


class BuyerTransactionList(APIView):
    @swagger_auto_schema(responses={200: TransactionSerializer(many=True)})
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        transactions = buyer_instance.as_payer_transactions.annotate(title=F('implementation__contract__ref_award__title'))
        data = TransactionSerializer(transactions, many=True).data
        return Response(data)


class BuyerRecordList(APIView):
    @swagger_auto_schema(responses={200: BuyerRecordSerializer(many=True)})
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        releases = Release.objects \
            .filter(
            buyer=buyer_instance,
        ).annotate(
            record_ocid=F('ref_record__ocid'),
            title=F('tender__title'),
            sector=F('ref_record__target__name'),
            country=F('ref_record__implementation_address__country_name'),
            region=F('ref_record__implementation_address__region'),
            value=F('ref_record__implementation_value__amount'),
            currency=F('ref_record__implementation_value__currency'),
            last_update=F('date')
        )
        data = BuyerRecordSerializer(releases, many=True).data
        return Response(data)

class RecordTransactionList(APIView):
    @swagger_auto_schema(responses={200: TransactionSerializer(many=True)})
    def get(self, request, record_id):
        record_instance = get_object_or_404(Record, pk=record_id)
        transactions = record_instance.compiled_release.buyer.as_payer_transactions.annotate(
            title=F('implementation__contract__ref_award__title')
        )
        data = TransactionSerializer(transactions, many=True).data
        return Response(data)




class RecordList(APIView):
    @swagger_auto_schema(responses={200: RecordSerializer(many=True)})
    def get(self, request):
        releases = Release.objects.all(
        ).annotate(
            record_id=F('ref_record__id'),
            record_ocid=F('ref_record__ocid'),
            title=F('tender__title'),
            buyer_name=F('buyer__name'),
            procuring_entity=F('tender__procuring_entity__name'),
            value=F('ref_record__implementation_value__amount'),
            currency=F('ref_record__implementation_value__currency'),
            country=F('ref_record__implementation_address__country_name'),
            region=F('ref_record__implementation_address__region'),
            sector=F('ref_record__target__name'),
        )
        data = RecordSerializer(releases, many=True).data
        return Response(data)

class RecordDetail(APIView):
    @swagger_auto_schema(responses={200: RecordSerializer(many=True)})
    def get(self, request, record_id):
        release = Release.objects.annotate(
            record_ocid=F('ref_record__ocid'),
            title=F('tender__title'),
            buyer_name=F('buyer__name'),
            procuring_entity=F('tender__procuring_entity__name'),
            value=F('ref_record__implementation_value__amount'),
            currency=F('ref_record__implementation_value__currency'),
            country=F('ref_record__implementation_address__country_name'),
            region=F('ref_record__implementation_address__region'),
            sector=F('ref_record__target__name'),
        ).get(ref_record__pk=record_id)
        data = RecordSerializer(release).data
        return Response(data)


class BuyerRecordSectorValues(APIView):
    @swagger_auto_schema(
        responses={200: BuyerRecordByStatusSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('start_year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('end_year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True)
        ]
    )
    def get(self, request, buyer_id):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        if start_year is None or end_year is None:
            return Response('Year not specified', status=500)
        if int(start_year) > int(end_year):
            return Response('Start year is after end year', status=500)

        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        records = Record.objects.filter(
            compiled_release__buyer=buyer_instance,
            compiled_release__tender__tender_period__start_date__year__gte=start_year,
            compiled_release__tender__tender_period__start_date__year__lte=end_year,
        ).values('compiled_release__tender__tender_period__start_date__year', sector=F('target__name')) \
            .annotate(value=Sum('implementation_value__amount'), currency=F('implementation_value__currency'))
        data = RecordSectorGroupedSerializer(records, many=True).data
        return Response(data)


class BuyerRecordByStatus(APIView):
    @swagger_auto_schema(
        responses={200: BuyerRecordByStatusSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, buyer_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        releases = Release.objects.filter(buyer=buyer_instance, tender__tender_period__start_date__year=year)
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
        data = BuyerRecordByStatusSerializer(output).data
        return Response(data)


class BuyerRecordValuesGrouped(APIView):
    @swagger_auto_schema(
        responses={200: BuyerRecordByStatusSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('group_by', openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=['region', 'sector'],
                              required=True)
        ]
    )
    def get(self, request, buyer_id):
        year = self.request.query_params.get('year')
        group_by = self.request.query_params.get('group_by')
        if year is None:
            return Response('Year not specified', status=500)
        if not group_by in ['region', 'sector']:
            return Response('Group field not specified', status=500)

        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        records = Record.objects.filter(
            compiled_release__buyer=buyer_instance,
            compiled_release__tender__tender_period__start_date__year=year
        )
        if group_by == 'region':
            records = records.annotate(
                name=Concat(
                    F('implementation_address__region'),
                    Value(', '),
                    F('implementation_address__country_name')
                )
            ).values('name')
        if group_by == 'sector':
            records = records.annotate(name=F('target__name')).values('name')
        records = records.annotate(value=Sum('implementation_value__amount'),
                                   currency=F('implementation_value__currency'))
        data = RecordValueGroupedSerializer(records, many=True).data
        return Response(data)


# Accueil

class RecordNumberByStatusYearView(APIView):
    @swagger_auto_schema(
        responses={200: RecordNumberByStatusYearSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request):
        year = self.request.query_params.get('year')

        if year is None:
            return Response('Year not specified', status=500)

        releases = Release.objects.filter(
            tender__tender_period__start_date__year=year
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


class RecordValueEvolutionBySectorView(APIView):
    @swagger_auto_schema(
        responses={200: RecordValueEvolutionBySectorSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('start_year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('end_year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
        ]
    )
    def get(self, request):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')

        if start_year is None or end_year is None:
            return Response('Year not specified', status=500)
        if int(start_year) > int(end_year):
            return Response('Start year is after end year', status=500)

        records = Record.objects.filter(
            compiled_release__tender__tender_period__start_date__year__gte=start_year,
            compiled_release__tender__tender_period__start_date__year__lte=end_year,
        ).values('compiled_release__tender__tender_period__start_date__year', sector=F('target__name')) \
            .annotate(value=Sum('implementation_value__amount'), currency=F('implementation_value__currency'))
        data = RecordValueEvolutionBySectorSerializer(records, many=True).data
        return Response(data)


class RecordValueByGenericView(APIView):
    @swagger_auto_schema(
        responses={200: RecordValueByGenericSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('group_by', openapi.IN_QUERY, type=openapi.TYPE_STRING, enum=['region', 'sector'],
                              required=True),
        ]
    )
    def get(self, request):
        year = self.request.query_params.get('year')
        group_by = self.request.query_params.get('group_by')

        if year is None:
            return Response('Year not specified', status=500)
        if not group_by in ['region', 'sector']:
            return Response('Group field not specified', status=500)

        records = Record.objects.filter(
            compiled_release__tender__tender_period__start_date__year=year
        )
        if group_by == 'region':
            records = records.annotate(
                name=Concat(
                    F('implementation_address__region'),
                    Value(', '),
                    F('implementation_address__country_name')
                )
            ).values('name')
        if group_by == 'sector':
            records = records.annotate(name=F('target__name')).values('name')
        records = records.annotate(value=Sum('implementation_value__amount'),
                                   currency=F('implementation_value__currency'))
        data = RecordValueByGenericSerializer(records, many=True).data
        return Response(data)


class AllRecordValueGroupByRegion(APIView):
    @swagger_auto_schema(
        responses={200: RecordValueByGenericSerializer(many=True)},
    )
    def get(self, request):
        records = Record.objects.all()
        records = records.annotate(
            locality_long=F('implementation_address__locality_longitude'),
            locality_lat=F('implementation_address__locality_latitude'),
            name=Concat(
                F('implementation_address__region'),
                Value(', '),
                F('implementation_address__country_name')
            )
        ).values('name', 'locality_long', 'locality_lat')
        records = records.annotate(value=Sum('implementation_value__amount'),
                                   currency=F('implementation_value__currency'),
                                   )
        data = RecordValueByGenericSerializer(records, many=True).data
        return Response(data)


# End Accueil

class PublishedReleaseView(APIView):
    def get(self, request, pk):
        published_release_instance = get_object_or_404(PublishedRelease, pk=pk)
        return Response(json.loads(published_release_instance.release))


class RecordItemList(APIView):
    @swagger_auto_schema(responses={200: ItemSerializer})
    def get(self, request, record_id):
        record_instance = get_object_or_404(Record, pk=record_id)
        if record_instance.compiled_release is None:
            return Response(data={}, status=status.HTTP_501_NOT_IMPLEMENTED)
        if record_instance.compiled_release.tender is None:
            return Response(data={}, status=status.HTTP_501_NOT_IMPLEMENTED)
        items = record_instance.compiled_release.tender.items.all()
        data = ItemSerializer(items, many=True).data
        return Response(data)


class RecordStageList(APIView):
    @swagger_auto_schema(responses={200: RecordStageSerializer})
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
    @swagger_auto_schema(responses={200: RecordSerializer(many=True)})
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        queryset = Record.objects.filter(compiled_release__buyer=buyer_instance.pk).exclude(
            compiled_release__tag__contains=['contractTermination'])
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)


class DoneRecordList(APIView):
    @swagger_auto_schema(responses={200: RecordSerializer(many=True)})
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        queryset = Record.objects.filter(
            compiled_release__buyer=buyer_instance.pk,
            compiled_release__tag__contains=['contractTermination']
        )
        data = RecordSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)


class SumRecord(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(name='region', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    def get(self, request):
        region = self.request.query_params.get('region')
        queryset = Record.objects.filter(
            implementation_address__region__iexact=region
        )
        data = RecordSumSerializer(queryset, many=True, context={'request': request}).data
        return Response({
            'entity': data
        })


class BuyerTotalRecord(APIView):
    @swagger_auto_schema(responses={200: RecordSerializer(many=True)})
    def get(self, request, buyer_id):
        buyer_instance = get_object_or_404(Entity, pk=buyer_id)
        queryset_progress = Release.objects.filter(
            buyer=buyer_instance.pk).exclude(tag=['contractTermination'])
        queryset_done = Release.objects.filter(
            buyer=buyer_instance.pk,
            tag=['contractTermination']
        )
        total_in = queryset_progress.count()
        total_finish = queryset_done.count()
        # output_instance['total'] = queryset_progress.count()+queryset_done.count()
        # data = BuyerRecordTotalSerializer(output_instance, many=True, context={'request': request}).data
        return Response({
            'In_progress': total_in,
            'Finish': total_finish
        })
