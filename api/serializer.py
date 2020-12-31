from rest_framework import serializers
from django.contrib.auth.models import User
from contact.models import Contact
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True, required=False)

    username = serializers.CharField(required=False)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that email already exists.")], required=False)

    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)

        user.save()

        contact = Contact(profile=True, nickname=user.email, email=user.email, owner=user)

        contact.save()

        return user

    def update(self, user, data):
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)

        password = data.get('password', None)
        if password is not None:
            user.set_password(password)

        user.save()

        return user

    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'email')