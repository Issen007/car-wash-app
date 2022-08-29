# Default Django Modules
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Apps Specific
from core.models import work, workType

# Serializers
from .serializers import WorkSerializer, WorkTypeSerializer

# Logging
import logging
log = logging.getLogger(__name__)

class WorkViewSet(ModelViewSet):
    serializer_class = WorkSerializer
    # if TEST == 0:
    #     permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = CoreConfig.objects.filter(user=self.request.user)
    #     return queryset

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # else:
    queryset = work.objects.all()

class WorkTypeViewSet(ModelViewSet):
    serializer_class = WorkTypeSerializer
    queryset = workType.objects.all()
