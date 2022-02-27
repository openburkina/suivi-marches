from ocds_awards.models import Award
from ocds_master_tables.serializers import (
    AmendmentSerializer,
    DocumentSerializer,
    EntitySerializer,
    ItemSerializer,
    PeriodSerializer,
    ValueSerializer,
)
from ocds_contracts.serializers import ContractSerializer

from rest_framework import serializers


class AwardSerializer(serializers.ModelSerializer):
    value = ValueSerializer()
    contract_period = PeriodSerializer()
    suppliers = EntitySerializer(many=True)
    items = ItemSerializer(many=True)
    documents = DocumentSerializer(many=True)
    amendments = AmendmentSerializer(many=True)
    contract = ContractSerializer()

    class Meta:
        model = Award
        exclude = ['id']

class AwardPeriodSerializer(serializers.ModelSerializer):
    contract_period = PeriodSerializer()

    class Meta:
        model = Award
        fields = ['id', 'date', 'contract_period']
