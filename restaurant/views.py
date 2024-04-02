from django.shortcuts import render
from .serializers import MenuSerializer, ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from .models import Menu, Reservation

# Create your views here.
def home(request):
    return render(request, 'restaurant/home.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    