from rest_framework import viewsets
from .models import Label
from .serializer import LabelSerializer

class LabelApi(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer