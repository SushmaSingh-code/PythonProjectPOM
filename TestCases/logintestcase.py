import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys

sys.path.append("C:/Users/sushmasingh/PycharmProjects/POM")
from Pages.loginpage import loginpage


class loginTest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="..\\Drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = loginpage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clicklogin()
        time.sleep(20)
        #self.assertEqual("Dashboard /nopCommerce administration", self.driver.title, "webpage title is not matched")
        self.assertEqual("Your store. Login", self.driver.title, "webpage title is not matched")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..//Report"))
