from rest_framework import viewsets
from api.serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )