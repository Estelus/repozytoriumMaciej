# SUBTASK 4 NIESTETY NIE ZDAZYŁEM ZROBIĆ. ZAPOMNIAŁEM SIĘ I ZACZĄŁEM ROBIĆ ZADANIA DOPIERO WE WTOREK PO 20.00.
# PRZEPRASZAM


import os
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
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

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