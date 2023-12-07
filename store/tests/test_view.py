from django.test import TestCase,Client
from django.urls import reverse
from store.models import Product


class StoreViewTest(TestCase):
    def setUp(self):
        #Set up data for test
        Product.objects.create(name="testproduct",price=10.00)
        self.client=Client()

    def test_store_view(self):
        #test the store view
        #reverse function is used to generate URLs
        response=self.client.get(reverse('store'))
        # check if response is ok
        self.assertEqual(response.status_code,200)
        # check if the template used
        self.assertTemplateUsed(response,'store/store.html')
        # check if the 'product' is in context
        self.assertIn('products',response.context)


