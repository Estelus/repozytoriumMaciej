import os
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
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
    def test_log_in_to_the_system_with_invalid_password(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test1234")
        user_login.wait_for_button_to_be_clickable(user_login.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()
        user_login.wait_for_element_to_be_visible(user_login.invalid_data_caption_xpath)
        user_login.assert_element_text(self.driver, user_login.invalid_data_caption_xpath,
                                       user_login.invalid_password_text)

    @classmethod
    def tearDown(self):
        self.driver.quit()