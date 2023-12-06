from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Customer

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

