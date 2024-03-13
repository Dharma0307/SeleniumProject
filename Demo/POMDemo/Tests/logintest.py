from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from Demo.POMDemo.Pages.loginPage import LoginPage
from Demo.POMDemo.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_login_valid(self):
        # driver = self.driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home = HomePage(self.driver)
        # home.welcome_link_id()
        home.click_welcome()
        home.logout_link()
        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sdharmat/PycharmProjects/Selenium/Demo/reports'))

# java -jar jenkins.war --httpPort=9090
