from django.test import TestCase
from django.urls import reverse
from store.models import Order,Product,OrderItem, Customer
from django.contrib.auth.models import User

class UpdateItemViewTest(TestCase):
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Create a Customer instance and associate it with the User
        Customer.objects.create(user=self.user, name="Test Customer", email="test@example.com")

        # Create a Product instance
        Product.objects.create(name="Test Product", price=10.00)

        # Login with the created User
        self.client.login(username='testuser', password='12345')

    def test_update_item_add(self):
        #retrive the first product created in the setUp method
        product = Product.objects.first()
        # send a post requiest to the 'update_view'
        # this simulate a user action of adding a product to their order
        # The 'productId' and 'action' are included in the request's body
        response = self.client.post(reverse('update_item'), {'productId': product.id, 'action': 'add'}, content_type='application/json')
        #assert that the response status code is 200 if request is a success
        self.assertEqual(response.status_code, 200)
        # check if the OrderItem is created and set to 1
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(OrderItem.objects.first().quantity, 1)

        