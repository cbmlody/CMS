import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ccms(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()