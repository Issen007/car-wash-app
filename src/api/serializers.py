# Django Core Modules
from rest_framework import serializers

# Apps specific
from core.models import work, workType
from notification.models import EmailSettings

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = work
        fields = '__all__'

class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = workType
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSettings
        fields = '__all__'