from ocds_awards.serializers import AwardPeriodSerializer, AwardSerializer
from ocds_master_tables.serializers import (
    EntitySerializer,
    ItemSerializer,
    PeriodSerializer,
)
from ocds_release.constants import PARTY_ROLE
from ocds_release.models import Record, Release, Target
from rest_framework import serializers


class ReleaseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:release-detail")
    ref_record = serializers.HyperlinkedRelatedField(view_name="api:record-detail", read_only=True)
    tender = serializers.HyperlinkedRelatedField(view_name="api:tender-detail", read_only=True)
    planning = serializers.HyperlinkedRelatedField(view_name="api:planning-detail", read_only=True)
    buyer = EntitySerializer()
    awards = AwardSerializer(many=True)
    parties = EntitySerializer(many=True)

    class Meta:
        model = Release
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:record-detail")
    compiled_release = serializers.HyperlinkedRelatedField(view_name="api:release-detail", read_only=True)
    releases = serializers.HyperlinkedRelatedField(view_name="api:published-release-detail", read_only=True, many=True)

    class Meta:
        model = Record
        fields = '__all__'

class RecordStageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tender_period = PeriodSerializer()
    award_period = PeriodSerializer()
    awards = AwardPeriodSerializer(many=True)

class RecordItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tender = serializers.HyperlinkedRelatedField(view_name="api:tender-detail", read_only=True)
    items = ItemSerializer(many=True)

class RecordByTargetSerializer(serializers.Serializer):
    records = serializers.HyperlinkedRelatedField(view_name="api:record-detail", read_only=True, many=True)

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        exclude = ['id']

class RecordSumSerializer(serializers.ModelSerializer):
    #value = ValueSerializer()
    class Meta:
        model = Record
        fields ='__all__'
