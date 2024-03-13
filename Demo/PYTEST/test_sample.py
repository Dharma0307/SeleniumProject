from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.close()
        driver.quit()
        print("test completed")
    def test_login(self, test_setup):
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        x = driver.title
        assert x == 'OrangeHRM'


# def test_logout():
#     driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
#     driver.find_element(By.LINK_TEXT, "Logout").click()


# def tearDownClass():
#     driver.close()
#     driver.quit()
#     print("test completed")
