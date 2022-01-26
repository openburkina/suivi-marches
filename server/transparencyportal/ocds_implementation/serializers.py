from rest_framework import serializers

from ocds_master_tables.serializers import EntitySerializer, ValueSerializer
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    value = ValueSerializer()
    payer = EntitySerializer()
    payee = EntitySerializer()

    class Meta:
        model = Transaction
        exclude = ['id', 'implementation']
