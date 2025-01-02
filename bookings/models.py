from django.db import models
from django.utils import timezone

class Table(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=1)  # Provide a valid table ID here
    status = models.CharField(
        max_length=20,
        default='pending',
        choices=[('confirmed', 'Confirmed'), ('pending', 'Pending')]
    )
    booking_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking for {self.customer} at {self.table} on {self.booking_time}"


class BookingHistory(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    change_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
        default='confirmed'  # Set a default status
    )

    def __str__(self):
        return f"History for booking {self.booking} at {self.change_time}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
