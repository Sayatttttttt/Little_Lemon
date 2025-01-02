# orders/models.py
from django.db import models
from menu.models import MenuItem
from bookings.models import Booking

class Order(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for booking {self.booking.id} - Total: {self.total_amount}"
