from rest_framework import serializers

from ocds_master_tables.serializers import AmendmentSerializer, DocumentSerializer, ItemSerializer, MilestoneSerializer, PeriodSerializer, ValueSerializer
from ocds_contracts.models import Contract

class ContractSerializer(serializers.ModelSerializer):
    period = PeriodSerializer()
    value = ValueSerializer()
    items = ItemSerializer(many=True)
    documents = DocumentSerializer(many=True)
    milestones = MilestoneSerializer(many=True)
    amendments = AmendmentSerializer(many=True)

    class Meta:
        model = Contract
        fields = ['__all__']
        exclude = ['id']
