# Default Django Modules
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Apps Specific
from core.models import work, workType
from notification.models import EmailSettings, SMSSettings

# Serializers
from .serializers import (
    WorkSerializer, 
    WorkTypeSerializer,
    EmailSerializer,
    SMSSerializer,
    )
    

# Logging
import logging
log = logging.getLogger(__name__)

class WorkViewSet(ModelViewSet):
    serializer_class = WorkSerializer
    queryset = work.objects.all()

class WorkTypeViewSet(ModelViewSet):
    serializer_class = WorkTypeSerializer
    queryset = workType.objects.all()

class EmailViewSet(ModelViewSet):
    serializer_class = EmailSerializer
    queryset = EmailSettings.objects.all()

class SMSViewSet(ModelViewSet):
    serializer_class = SMSSerializer
    queryset = SMSSettings.objects.all()