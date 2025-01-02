from django.urls import path
from . import views
from .views import BookingListCreateView, BookingDetailView, BookingApiRootView


urlpatterns = [
    path('', views.booking_list, name='booking_list'),  # List of bookings
    path('create/', views.booking_create, name='booking_create'),  # Create a new booking
    path('update/<int:pk>/', views.booking_update, name='booking_update'),  # Update an existing booking
    path('delete/<int:pk>/', views.booking_delete, name='booking_delete'),  # Delete a booking
    path('api/', BookingApiRootView.as_view(), name='booking-api-root'),
    path('api/bookings/', views.BookingListCreateView.as_view(), name='booking-list-create'),
    path('api/bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
]
