from django.test import TestCase
from django.urls import reverse
from store.models import Product,Order,Customer,Post,OrderItem
from django.contrib.auth.models import User



class StoreViewTest(TestCase):
    # Test the store view with the store.html template.
    def test_store_view(self):
        # Send a GET request to the 'store' URL and capture the response.
        response = self.client.get(reverse('store'))

        # Check if the response status code is 200 (OK), indicating the view is working correctly.
        self.assertEqual(response.status_code, 200)

        # Verify that the response used the correct template ('store/store.html').
        self.assertTemplateUsed(response, 'store/store.html')




class FrontpageViewTest(TestCase):
    # Test the frontpage view with the frontpage.html template.
    def test_frontpage_view(self):
        # Send a GET request to the 'frontpage' URL and capture the response.
        response = self.client.get(reverse('frontpage'))

        # Check if the response status code is 200 (OK).
        self.assertEqual(response.status_code, 200)

        # Verify that the 'frontpage.html' template was used in the response.
        self.assertTemplateUsed(response, 'store/frontpage.html')


class BlogViewTest(TestCase):
    def setUp(self):
        # Create a test user and a test blog post for use in the test_blog_view method.
        User.objects.create_user('testuser', 'test@example.com', 'password')
        Post.objects.create(author=User.objects.first(), title="Test Post", text="Test content")

    # Test the blog view with the blog.html template.
    def test_blog_view(self):
        # Send a GET request to the 'blog' URL and capture the response.
        response = self.client.get(reverse('blog'))

        # Check if the response status code is 200 (OK).
        self.assertEqual(response.status_code, 200)

        # Verify that the 'blog.html' template was used.
        self.assertTemplateUsed(response, 'store/blog.html')

        # Ensure that 'posts' are included in the context passed to the template.
        self.assertIn('posts', response.context)



class UpdateItemViewTest(TestCase):
    def setUp(self):
        # Create a test user, customer, and product for the test_update_item_add method.
        user = User.objects.create_user(username='testuser', password='12345')
        Customer.objects.create(user=user, name="Test Customer", email="test@example.com")
        Product.objects.create(name="Test Product", price=10.00)

    # Test the updateItem view for adding an item.
    def test_update_item_add(self):
        # Log in as the test user.
        self.client.login(username='testuser', password='12345')

        # Retrieve the first product instance.
        product = Product.objects.first()

        # Send a POST request to 'update_item' view, simulating adding a product.
        response = self.client.post(reverse('update_item'), {'productId': product.id, 'action': 'add'}, content_type='application/json')

        # Verify the response status code is 200 (OK).
        self.assertEqual(response.status_code, 200)

        # Check if one OrderItem has been created in the database.
        self.assertEqual(OrderItem.objects.count(), 1)

        # Check if the quantity of the first OrderItem is set to 1.
        self.assertEqual(OrderItem.objects.first().quantity, 1)

