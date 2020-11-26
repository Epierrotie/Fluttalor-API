from rest_framework import serializers
from contact.serializer import ContactSerializer
from .models import Label

class LabelSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='pk', required=False)
    name = serializers.CharField(max_length=45)

    def create(self, validated_data):
        label = Label.objects.create(**validated_data)

        label.save()

        return label

    def update(self, label, validated_data):
        label.name = validated_data.get('name', label.name)

        label.save()

        return label

    class Meta:
        model = Label
        fields = ("__all__")