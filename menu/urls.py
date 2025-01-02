from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, MenuItemListCreateView, MenuItemDetailView
from . import views

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('menu/', views.menu_view, name='menu'),
    path('<int:id>/', views.menu_item_view, name='menu_item'),
    path('api/menu/', MenuItemListCreateView.as_view(), name='menu-list-create'),
    path('api/menu/<int:pk>/', MenuItemDetailView.as_view(), name='menu-detail'),
]
