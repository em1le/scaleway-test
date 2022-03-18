from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from hardware.models import Hardware
from hardware.serializers import HardwareSerializer


class HardwareViewSet(viewsets.ModelViewSet):
    serializer_class = HardwareSerializer
    permission_classes = [IsAuthenticated]
    queryset = Hardware.objects.all()
