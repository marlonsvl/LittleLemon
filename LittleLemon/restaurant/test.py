from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        MenuItem.objects.create(title='Cheese pinaple', price=100, inventory=100)
    def test_get_item(self):
        ice = MenuItem.objects.get(title="IceCream")
        cheese = MenuItem.objects.get(title="Cheese pinaple")
        self.assertEqual(f'{ice.title} : {ice.price}', "IceCream : 80.00")
        self.assertEqual(f'{cheese.title} : {cheese.price}', "Cheese pinaple : 100.00")
        