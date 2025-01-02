from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm
from .serializers import BookingSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import generics


# Django Views for Web Interface

@login_required
def booking_list(request):
    bookings = Booking.objects.all()  # Get all bookings
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)  # Use a form to handle the POST data
        if form.is_valid():
            form.save()  # Save the new booking
            return redirect('booking_list')  # Redirect to the booking list after saving
    else:
        form = BookingForm()  # If it's a GET request, show an empty form
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# bookings/views.py
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class BookingApiRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to the bookings API!"})
