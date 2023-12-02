from django.test import TestCase
from . import views

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title='IceCream2', price=80, inventory=100)
        MenuItem.objects.create(title='Cheese pinaple2', price=100, inventory=100)
    
    def test_getall():
        all = MenuItem.objects.all()
        self.assertEqual(2,2)