from rest_framework import serializers
from .models import Amount, Budget, Planning, PlanningDocument
from .abstract_models import Document

class AmountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Amount
        fields = '__all__'

class BudgetSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Budget
        fields = '__all__'

class PlanningSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Planning
        fields = '__all__'

class PlanningDocumentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = PlanningDocument
        fields = '__all__'

class DocumentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Document
        fields = '__all__'