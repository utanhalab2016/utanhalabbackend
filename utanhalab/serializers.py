from rest_framework import serializers
from .models import PrincipalModel
class UtanhalabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrincipalModel
        fields = ('calendario', 'quantidade')


