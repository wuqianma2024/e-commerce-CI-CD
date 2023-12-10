from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class MyE2ETest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_flow(self):
        # Example: User visits the homepage
        self.selenium.get(f'{self.live_server_url}/')
        print(self.selenium.title)
        self.assertIn("SHARE TO EARN", self.selenium.title)
       


  
            