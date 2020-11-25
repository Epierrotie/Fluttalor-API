from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='pk')
    nickname = serializers.CharField(max_length=45, allow_null=True, required=False)
    firstname = serializers.CharField(max_length=45, allow_null=True, required=False)
    lastname = serializers.CharField(max_length=45, allow_null=True, required=False)

    email = serializers.EmailField(max_length=255, allow_null=True)
    phone = serializers.CharField(max_length=255, allow_null=True)

    def create(self, validated_data):
        if 'nickname' not in validated_data and 'firstname' not in validated_data and 'lastname' not in validated_data:
            raise serializers.ValidationError("You must assign at least one of those : a firstname, lastname or nickname")
        contact = Contact.objects.create(**validated_data)

        contact.save()

        return contact

    def update(self, contact, validated_data):

        contact.nickname = validated_data.get('nickname', contact.nickname)
        contact.firstname = validated_data.get('firstname', contact.firstname)
        contact.lastname = validated_data.get('lastname', contact.lastname)

        contact.email = validated_data.get('email', contact.email)
        contact.phone = validated_data.get('phone', contact.phone)

        contact.save()
        return contact

    class Meta:
        model = Contact
        fields = ('__all__')