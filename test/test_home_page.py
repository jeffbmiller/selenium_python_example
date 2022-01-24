from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestHomePage(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)       

    def test_home_page_title(self):
        self.driver.get("http://seedtrakr.com")
        title = self.driver.title
        assert title == "Seedtrakr | Seed Management Solution", "Home Page Title Incorrect"       

    def test_pricing_link(self):
        self.driver.get("http://seedtrakr.com")
        pricing_link = self.driver.find_element(By.LINK_TEXT, 'Pricing')
        pricing_link.click()
        sleep(3)
        title = self.driver.title
        assert title == "Pricing — Seedtrakr | Seed Management Solution" , "Pricing Page Title Incorrect"

    def test_require_captcha(self):
        self.driver.get("http://seedtrakr.com")
        link = self.driver.find_element(By.LINK_TEXT, 'Contact')
        link.click()
        sleep(3)
        full_name = self.driver.find_element(By.ID, 'text-yui_3_17_2_1_1544715708870_29146-field')
        full_name.send_keys('Jeff Miller')

        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys('jeff@rimmertechpartners.com')

        send_btn = self.driver.find_element(By.CLASS_NAME, 'button')
        send_btn.click()

        captacha_div = self.driver.find_element(By.CLASS_NAME, 'field-error')
        assert captacha_div.text == 'Complete CAPTCHA before submitting.'

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()