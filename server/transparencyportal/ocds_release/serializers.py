from rest_framework import serializers

from ocds_release.models import Record, Release
from ocds_master_tables.serializers import PeriodSerializer, EntitySerializer
from ocds_awards.serializers import AwardPeriodSerializer

class ReleaseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:release-detail")
    ref_record = serializers.HyperlinkedRelatedField(view_name="api:record-detail", read_only=True)
    tender = serializers.HyperlinkedRelatedField(view_name="api:tender-detail", read_only=True)
    buyer = EntitySerializer()
    class Meta:
        model = Release
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:record-detail")
    compiled_release = serializers.HyperlinkedRelatedField(view_name="api:release-detail", read_only=True)
    class Meta:
        model = Record
        fields = '__all__'

class RecordStageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tender_period = PeriodSerializer()
    award_period = PeriodSerializer()
    awards = AwardPeriodSerializer(many=True)
