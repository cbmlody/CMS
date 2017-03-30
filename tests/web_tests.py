import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ccms(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")
        self.driver.maximize_window()

    def test_a_admin_login(self):
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("admin")
        elem2 = self.driver.find_element_by_name("password")
        elem2.send_keys("1234")
        time.sleep(1)
        elem2.send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertTrue('id="error"' not in self.driver.page_source)

    def test_b_create_mentor(self):
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("admin")
        elem2 = self.driver.find_element_by_name("password")
        elem2.send_keys("1234")
        time.sleep(1)
        elem2.send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertTrue('id="error"' not in self.driver.page_source)
        self.driver.find_element_by_xpath("//a[contains(@href,'/mentor')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@href='/mentor/add']").click()
        name = self.driver.find_element_by_name("fullname")
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("pass")
        rpass = self.driver.find_element_by_name("rpass")
        name.send_keys("marcin izworski")
        username.send_keys('marcinizw')
        password.send_keys("1234")
        rpass.send_keys("1234")
        self.driver.find_element_by_xpath("html/body/div[1]/div/div/div/form/input[5]").click()
        self.assertTrue('<td>mentor</td>' not in self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()