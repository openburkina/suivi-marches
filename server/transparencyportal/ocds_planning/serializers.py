from rest_framework import serializers
from .models import Planning, PlanningDocument

class PlanningSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Planning
        fields = '__all__'

class PlanningDocumentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = PlanningDocument
        fields = '__all__'
