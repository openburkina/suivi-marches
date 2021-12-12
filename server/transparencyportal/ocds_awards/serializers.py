from rest_framework import serializers

from ocds_awards.models import Award
from ocds_master_tables.serializers import AmendmentSerializer, DocumentSerializer, ItemSerializer, EntitySerializer, PeriodSerializer, ValueSerializer

class AwardSerializer(serializers.ModelSerializer):
    value = ValueSerializer()
    contract_period = PeriodSerializer()
    suppliers = EntitySerializer(many=True)
    items = ItemSerializer(many=True)
    documents = DocumentSerializer(many=True)
    amendments = AmendmentSerializer(many=True)

    class Meta:
        model = Award
        exclude = ['id']

class AwardPeriodSerializer(serializers.ModelSerializer):
    contract_period = PeriodSerializer()

    class Meta:
        model = Award
        fields = ['date', 'contract_period']
