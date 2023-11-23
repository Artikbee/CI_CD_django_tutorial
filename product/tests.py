from django.test import TestCase

from . import models


class ProductTest(TestCase):
    def test_first_object_in_db(self):
        obj1 = models.Product.objects.first()
        self.assertEquals(obj1.name, 'T-shirt')

    def test_second_object_in_db(self):
        obj1 = models.Product.objects.get(pk=2)
        self.assertEquals(obj1.name, 'Hoodie')
