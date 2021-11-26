from rest_framework import serializers

from ocds_release.models import Record, Release
from ocds_master_tables.serializers import PeriodSerializer
from ocds_awards.serializers import AwardPeriodSerializer

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class RecordStageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tender_period = PeriodSerializer()
    award_period = PeriodSerializer()
    awards = AwardPeriodSerializer(many=True)
