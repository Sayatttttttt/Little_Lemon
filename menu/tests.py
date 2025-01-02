# menu/tests.py
from django.test import TestCase
from menu.models import MenuItem

class MenuItemTestCase(TestCase):
    def setUp(self):
        # Create sample menu items for testing
        MenuItem.objects.create(name='Pizza Margherita', description='Classic pizza with fresh mozzarella and basil.', price=12.99)
        MenuItem.objects.create(name='Spaghetti Carbonara', description='Pasta with creamy sauce and pancetta.', price=14.99)

    def test_menu_item_count(self):
        # Test that the menu has two items
        items = MenuItem.objects.all()
        self.assertEqual(items.count(), 2)

    def test_menu_item_name(self):
        # Test that the menu item has the correct name
        pizza = MenuItem.objects.get(name='Pizza Margherita')
        self.assertEqual(pizza.name, 'Pizza Margherita')
