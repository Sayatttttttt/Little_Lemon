# bookings/serializers.py
from rest_framework import serializers
from users.models import User  # Adjust if the model is named differently
from bookings.models import Booking  # If you also want to include bookings

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']  # Adjust to your model fields

class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'customer', 'date', 'details']  # Example fields
