from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Customer, Product, Order,OrderItem

class CustomerModelTest(TestCase):

    # setUp runs before each test method to set up environment
    def setUp(self):
        #create a user test
        User.objects.create_user('testuser','test@example.com','password')
        #create a customer instance linked to the test user
        Customer.objects.create(user=User.objects.get(username='testuser'),name="Test Customer",email="testcustomer@example.com")
    

    # test if the custoemr instance is created
    def test_customer_creation(self):
        # retrive the customer created in setUp
        customer=Customer.objects.get(name="Test Customer")
        # assert the customer's email is what we expected
        self.assertEqual(customer.email,"testcustomer@example.com")
    

    # check the imnformation of the test customer
    def test_customer_str(self):
        # retrive the customer created in setUp
        customer=Customer.objects.get(name="Test Customer")
        # assert the name of customer is matching with this string
        self.assertEqual(str(customer),"Test Customer")




class ProductModelTest(TestCase):
    
    # set up a method for create a product instance to be tested
    def setUp(self):
        Product.objects.create(name="Test Product",price=9.99)

    #check if the product is created
    def test_product_creation(self):
        product=Product.objects.get(name="Test Product")
        self.assertEqual(product.price,9.99)

    #check the name of the created product's name
    def test_product_str(self):
        product=Product.objects.get(name="Test Product")
        self.assertEqual(str(product),"Test Product")
    
    #test the imageURL property of the Product
    #assert that the imageURL is by default ''(if no image)
    #test to handle image missing occation
    def test_image_url(self):
        product=Product.objects.get(name="Test Product")
        self.assertEqual(product.imageURL,'')


class OrderModelTest(TestCase):

    #setup the necessary instances for test
    def setUp(self):
        #create a product instance
        product=Product.objects.create(name="Test Product",price=9.99,digital=False)
        #create an empty order instance
        order=Order.objects.create(customer=Customer.objects.first(),complete=False)
        #create an OrderItem instance to complete an order
        #it links order and product instance
        order=OrderItem.objects.create(product=product,order=order,quantity=2)
        #create customer instance
        Customer.objects.create(name="Test Customer",email="testcustomer@example.com")
    

    #test the 'shipping' property of the Order model
    def test_order_shipping(self):
        #since order is default with shipping
        #only default non-digital Product
        order=Order.objects.first()
        self.assertTrue(order.shipping)

    #test the 'get_cart_total' property
    #it should caculate the total cost of the order
    def test_get_cart_total(self):
        order=Order.objects.first()
        self.assertEqual(order.get_cart_total,19.98)

    
    #test the 'get_cart_items' property
    #it should return the total number of items in the order
    def test_get_cart_items(self):
        order=Order.objects.first()
        self.assertEqual(order.get_cart_items,2)






