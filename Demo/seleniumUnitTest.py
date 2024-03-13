import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.NAME, "q").send_keys("Python tutorials")
        self.driver.find_element(By.NAME, "btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Python tutorials - Google Search")

    def test_search_2(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.NAME, "q").send_keys("Pycharm tutorials")
        self.driver.find_element(By.NAME, "btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Pycharm tutorials - Google Search")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()






    #
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
