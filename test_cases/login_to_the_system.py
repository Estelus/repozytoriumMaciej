import os
<<<<<<< Updated upstream
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage


from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')



class TestLogInPage(unittest.TestCase):


    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
=======
import unittest

from driver import driver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLogInPage(unittest.TestCase):

    @classmethod
    def setup(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = WebDriver.Chrome(service=self.driver_service)
>>>>>>> Stashed changes
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

<<<<<<< Updated upstream
    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
=======
    def test_log_in_the_system(self):
        user_login = LoginPage(driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_will_be_clickable()
        user_login.click_on_sign_in_button()
>>>>>>> Stashed changes
