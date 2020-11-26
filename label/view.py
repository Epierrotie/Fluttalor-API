from rest_framework import viewsets
from .models import Label
from .serializer import LabelSerializer
from rest_framework.response import Response
from rest_framework import status

class LabelApi(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def create(self, request):
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)