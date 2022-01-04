from ocds_master_tables.serializers import (
    AmendmentSerializer,
    EntitySerializer,
    ItemSerializer,
    MilestoneSerializer,
    PeriodSerializer,
    ValueSerializer,
)
from ocds_tender.models import Tender, TenderDocument, TenderItem, TenderMilestone
from rest_framework import serializers


class TenderDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderDocument
        fields = '__all__'

class TenderSerializer(serializers.ModelSerializer):
    buyer = EntitySerializer()
    min_value = ValueSerializer()
    value = ValueSerializer()
    tender_period = PeriodSerializer()
    enquiry_period = PeriodSerializer()
    award_period = PeriodSerializer()
    procuring_entity = EntitySerializer()
    amendments = AmendmentSerializer(many=True)
    items = ItemSerializer(many=True)
    documents = TenderDocumentSerializer(many=True)
    milestones = MilestoneSerializer(many=True)
    tenderers = EntitySerializer(many=True)
    number_of_tenderer = serializers.IntegerField()

    class Meta:
        model = Tender
        fields = '__all__'


class TenderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderItem
        fields = '__all__'


class TenderMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderMilestone
        fields = '__all__'

class RatingSerializer(serializers.Serializer):
    region_name = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()
    buyer_name = serializers.ReadOnlyField()

class TenderStateMount(serializers.ModelSerializer):
    value = ValueSerializer()
    class Meta:
        model = Tender
        fields = ('title','value',
        'status')
