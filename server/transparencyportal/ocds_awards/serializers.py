from rest_framework import serializers

from ocds_awards.models import Award
from ocds_master_tables.serializers import PeriodSerializer

class AwardPeriodSerializer(serializers.ModelSerializer):
    contract_period = PeriodSerializer()

    class Meta:
        model = Award
        fields = ['date', 'contract_period']
