from django.test import TestCase,Client
from django.urls import reverse
from store.models import Product,User,Post,Customer,Order,OrderItem


"""
view testing is for the backend testing
"""

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


class BlogViewTest(TestCase):
    def setUp(self):
        # Create a couple of sample posts for the test
        user = User.objects.create_user('testuser', 'test@example.com', 'password')
        Post.objects.create(author=user, title="Test Post 1", text="Test content 1")
        Post.objects.create(author=user, title="Test Post 2", text="Test content 2")

    def test_blog_view(self):
        #test the blog view
        response = self.client.get(reverse('blog'))
        #assert the response status code is 200(OK)
        self.assertEqual(response.status_code, 200)
        #assert that the correct template is used for the blog view
        self.assertTemplateUsed(response, 'store/blog.html')
        #assert the number of posts is correct
        self.assertEqual(len(response.context['posts']), 2)  
    

class UpdateItemViewTest(TestCase):
    def setUp(self):
        # Create necessary objects
        self.user = User.objects.create_user(username='testuser', password='12345')
        product = Product.objects.create(name="Test Product", price=10.00)
        customer = Customer.objects.create(user=self.user, name="Test Customer", email="test@example.com")
        order = Order.objects.create(customer=customer, complete=False)

    def test_update_item_add(self):

        #log in as the test user
        self.client.login(username='testuser', password='12345')
        #retrive the first product since we only have one
        product = Product.objects.first()
        #simulate a POST request to the update_item view
        #try to add the product into the order
        response = self.client.post(reverse('update_item'), 
                                    {'productId': product.id, 'action': 'add'}, 
                                    content_type='application/json')
        
        #check if the response status is 200
        self.assertEqual(response.status_code, 200)
        order_item = OrderItem.objects.first()
        #check the number of item
        self.assertEqual(order_item.quantity, 1)  # Assuming the item is added
