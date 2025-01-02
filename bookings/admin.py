from django.contrib import admin
from .models import Table, Booking, BookingHistory, Customer

admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(BookingHistory)
admin.site.register(Customer)
