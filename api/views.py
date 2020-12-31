from rest_framework import viewsets
from api.serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class UserApi(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated() and request.user.is_admin
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False


    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)