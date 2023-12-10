from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class MyE2ETest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-dev-shm-usage')
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
       


  
            