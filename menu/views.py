from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import generics



class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# View to display the entire menu
def menu_view(request):
    # Get all MenuItems
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})

# View to display a single MenuItem
def menu_item_view(request, id):
    # Get the MenuItem by id or 404 if not found
    menu_item = get_object_or_404(MenuItem, id=id)
    return render(request, 'menu/menu_item.html', {'menu_item': menu_item})
def home_view(request):
    return render(request, 'menu/home.html')

def about_view(request):
    return render(request, 'menu/about.html')


class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
