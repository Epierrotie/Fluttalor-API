from rest_framework import viewsets
from .models import Contact
from .serializer import ContactSerializer
from rest_framework.response import Response
from rest_framework import status

class ContactApi(viewsets.ModelViewSet):
    serializer_class = ContactSerializer

    def create(self, request):
        serializer = ContactSerializer(data=request.data, context={'owner': request.user})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk=None):
    #     print(request, pk)
    #     contact = Contact.objects.filter(pk=pk)
    #     serializer = ContactSerializer(data=request.data, context={'owner': request.user})
    #     if serializer.is_valid():
    #         serializer.update(contact=contact, data=request.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)