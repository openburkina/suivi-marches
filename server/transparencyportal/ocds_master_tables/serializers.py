from rest_framework import serializers
from .models import Address, Amendment, Change, Classification, ContactPoint, Document, Entity, Identifier, EntityAdditionalIdentifier, Item, ItemAdditionalClassification, Milestone, MilestoneDocument, Period, Unit, Value, Projet, Budget

class RegionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    country = serializers.CharField()
    region = serializers.CharField(source='name')

# Specific serializers. 
class RecordAggregateSerializer(serializers.Serializer):
    record_ocid = serializers.CharField()
    suppliers = serializers.ListField()
    title = serializers.CharField()
    sector = serializers.CharField()
    buyer_name = serializers.CharField()
    value = serializers.FloatField()
    currency = serializers.CharField()
    step = serializers.CharField()
    last_update = serializers.DateTimeField()

class RecordValueBySectorYearSerializer(serializers.Serializer):
    year = serializers.IntegerField(source='compiled_release__tender__tender_period__start_date__year')
    sector = serializers.CharField()
    value = serializers.FloatField()
    currency = serializers.CharField()

class RecordNumberByStatusYearSerializer(serializers.Serializer):
    planning = serializers.IntegerField()
    tender = serializers.IntegerField()
    award = serializers.IntegerField()
    contract = serializers.IntegerField()
    implementation = serializers.IntegerField()
    done = serializers.IntegerField()
    total = serializers.IntegerField()

class RecordValueEvolutionBySectorSerializer(serializers.Serializer):
    year = serializers.IntegerField(source='compiled_release__tender__tender_period__start_date__year')
    sector = serializers.CharField()
    value = serializers.FloatField()
    currency = serializers.CharField()

class RecordValueByGenericSerializer(serializers.Serializer):
    name = serializers.CharField()
    region_id = serializers.IntegerField(allow_null=True)
    value = serializers.FloatField()
    currency = serializers.CharField()
    locality_long = serializers.FloatField(allow_null=True)
    locality_lat = serializers.FloatField(allow_null=True)
# class RecordValueMapSerializer(serializers.Serializer):
# End specific serializers.

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AmendmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amendment
        fields = '__all__'


class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = '__all__'


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'


class ContactPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPoint
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = '__all__'

class EntitySerializer(serializers.ModelSerializer):
    identifier = IdentifierSerializer()
    address = AddressSerializer()
    contact_point = ContactPointSerializer()
    class Meta:
        model = Entity
        fields = '__all__'

class EntityAdditionalIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityAdditionalIdentifier
        fields = '__all__'

class ItemAdditionalClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAdditionalClassification
        fields = '__all__'

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class MilestoneDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneDocument
        fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        exclude =['id']

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        exclude =['id']

class UnitSerializer(serializers.ModelSerializer):
    value = ValueSerializer()
    class Meta:
        model = Unit
        exclude =['id']

class ItemSerializer(serializers.ModelSerializer):
    # classification = ClassificationSerializer()
    unit = UnitSerializer()
    class Meta:
        model = Item
        exclude = ['id', 'classification']

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
