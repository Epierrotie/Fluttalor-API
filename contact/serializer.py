from rest_framework import serializers
from .models import Contact
from .models import Label

class LabelContactSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    name = serializers.CharField(max_length=45)

    class Meta:
        model = Label
        fields = ("__all__")

class ContactSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True, required=False)
    nickname = serializers.CharField(max_length=45, allow_null=True, required=False)
    firstname = serializers.CharField(max_length=45, allow_null=True, required=False)
    lastname = serializers.CharField(max_length=45, allow_null=True, required=False)

    email = serializers.EmailField(max_length=255, allow_null=True, required=False)
    phone = serializers.CharField(max_length=255, allow_null=True, required=False)

    icon = serializers.ImageField(allow_null=True, required=False)

    labels = LabelContactSerializer(read_only=True, many=True)
    labels_id = serializers.PrimaryKeyRelatedField(queryset=Label.objects.all(), write_only=True, many=True, required=False)

    def create(self, validated_data):
        labels = validated_data.pop('labels_id')

        if 'nickname' not in validated_data and 'firstname' not in validated_data and 'lastname' not in validated_data:
            raise serializers.ValidationError("You must assign at least one of those : a firstname, lastname or nickname")
        contact = Contact.objects.create(**validated_data)

        contact.labels.set(labels)

        contact.save()

        return contact

    def update(self, contact, data):
        labels = data.pop('labels_id')

        contact.labels.set(labels)

        contact.nickname = data.get('nickname', contact.nickname)
        contact.firstname = data.get('firstname', contact.firstname)
        contact.lastname = data.get('lastname', contact.lastname)

        contact.email = data.get('email', contact.email)
        contact.phone = data.get('phone', contact.phone)

        contact.icon = data.get('icon', contact.icon)

        contact.save()
        return contact

    class Meta:
        model = Contact
        fields = ('__all__')