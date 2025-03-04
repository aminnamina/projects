from rest_framework import generics
from .models import Table
from .serializers import TableSerializer

class TableListCreateView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class AvailableTablesView(generics.ListAPIView):
    queryset = Table.objects.filter(is_available=True)
    serializer_class = TableSerializer

