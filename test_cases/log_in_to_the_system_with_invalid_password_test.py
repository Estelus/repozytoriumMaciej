import os
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.remind_password_page import RemindPasswordPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')

class TestSignOutFromSystem(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
        self.driver.get("https://scouts.futbolkolektyw.pl/en")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


    @classmethod
    def test_remind_password_form(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.click_on_the_remind_pw_button()
        remind_pw_page = RemindPasswordPage(self.driver)
        remind_pw_page.title_of_the_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()