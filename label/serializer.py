from rest_framework import serializers
from .models import Label

class LabelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=45)

    class Meta:
        model = Label
        fields = ("__all__")