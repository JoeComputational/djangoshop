from django.test import TestCase
from store.models import Category, Product

class TestCategoriesModel(TestCase):
    
    def setUp(self):
        self.data1 = Category.objects.create(name='Kidney Bean', slug='kidney-bean')

    def test_category_model_entry(self):
        #Test the category model naming scheme
        data = self.data1
        self.assertEqual(str(data), 'kidney-bean')

    def test_category_model_entry(self):
        #Test Category model data
        data = self.data1
        self.assertTrue(isinstance(data, Category))

