
from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from django.utils import timezone
from rest_framework.exceptions import ValidationError

class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        customer = serializer.validated_data['customer']
        date = serializer.validated_data['date']
        # Preventing overlapping reservations
        if Reservation.objects.filter(customer=customer, date=date).exists():
            raise ValidationError("User already has a reservation on this date.")
        serializer.save()

class ReservationDetailView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
