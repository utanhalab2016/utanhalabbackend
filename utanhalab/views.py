from rest_framework import viewsets
from .serializers import UtanhalabSerializer
from .models import PrincipalModel

class UtanhalabViewSet(viewsets.ModelViewSet):

        queryset = PrincipalModel.objects.all()
        serializer_class = UtanhalabSerializer





