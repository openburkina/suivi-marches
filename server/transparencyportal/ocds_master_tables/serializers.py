from rest_framework import serializers
from .models import Address, Amendment, Change, Classification, ContactPoint, Document, Entity, Identifier, EntityAdditionalIdentifier, Item, ItemAdditionalClassification, Milestone, MilestoneDocument, Organization, Period, Unit, Value, Projet, Budget


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

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    classification = ClassificationSerializer()
    unit = UnitSerializer()
    class Meta:
        model = Item
        fields = '__all__'

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
