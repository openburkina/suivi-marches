from rest_framework import serializers
from ocds_tender.models import Buyer, Tender, TenderDocument, Tenderer, TenderItem, TenderMilestone
from ocds_master_tables.serializers import AddressSerializer, AmendmentSerializer, ChangeSerializer, ClassificationSerializer, ContactPointSerializer, DocumentSerializer, EntitySerializer, IdentifierSerializer, EntityAdditionalIdentifierSerializer, ItemSerializer, ItemAdditionalClassificationSerializer, MilestoneSerializer, MilestoneDocumentSerializer, OrganizationSerializer, PeriodSerializer, UnitSerializer, ValueSerializer, ProjetSerializer, BudgetSerializer

class BuyerSerializer(EntitySerializer):
    class Meta:
        model = Buyer
        fields = '__all__'

class TenderDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderDocument
        fields = '__all__'

class TenderSerializer(serializers.ModelSerializer):
    buyer = BuyerSerializer()
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


class TendererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenderer
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
