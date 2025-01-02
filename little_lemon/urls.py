from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')), 
    path('', include('menu.urls')),  # Ensure this is include 
    path('api/auth/', include('djoser.urls')),  # for standard auth endpoints
    path('api/auth/', include('djoser.urls.jwt')),  # for JWT auth endpointsfrom django.urls import path, include
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)