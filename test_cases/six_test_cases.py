import os
import unittest

from PIL import Image
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.remind_password_page import RemindPasswordPage
from pages.AddPlayer import AddPlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')

class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
        self.driver.get("https://scouts.futbolkolektyw.pl/en")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def test_log_in_to_the_system_with_valid_data(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.wait_for_button_to_be_clickable(user_login.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()
    #   self.driver.save_screenshot(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\login_to_the_system/login-form-filled.png")
    #   Image.open(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\login-form-filled.png").show()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_the_page()

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
    #   self.driver.save_screenshot(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\login_to_the_system/invalid-password.png")
    #   Image.open(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\login_to_the_system/invalid-password.png").show()

    @classmethod
    def test_log_in_to_the_system_with_missing_login(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.wait_for_button_to_be_clickable(user_login.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()
        user_login.wait_for_element_to_be_visible(user_login.invalid_data_caption_xpath)
        user_login.assert_element_text(self.driver, user_login.invalid_data_caption_xpath,
                                       user_login.invalid_login_text)
    #   self.driver.save_screenshot(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\login_to_the_system/missing-login.png")
    #    Image.open(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\missing-login.png").show()

    @classmethod
    def test_remind_password_form(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.click_on_the_remind_pw_button()
        remind_pw_page = RemindPasswordPage(self.driver)
        remind_pw_page.title_of_the_page()
    #   self.driver.save_screenshot(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\remind-password.png")
    #   Image.open(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\remind-password.png").show()

    @classmethod
    def test_log_out_from_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.wait_for_button_to_be_clickable(user_login.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
    #   self.driver.save_screenshot(r'C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\dashboard-page.png')
    #   Image.open(r'C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\dashboard-page.png').show()
        dashboard_page.click_on_sign_out()
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
    #   self.driver.save_screenshot(r"C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\signed-out.png")
    #   Image.open(r'C:\Users\macie\OneDrive\Dokumenty\GitHub\repozytoriumMaciej\test_cases\screenshots\signed-out.png').show()
    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_the_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.wait_for_button_to_be_clickable(user_login.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_the_page()
        dashboard_page.click_on_add_player()
        add_a_player = AddPlayerPage(self.driver)
        add_a_player.type_in_name('Janusz')
        add_a_player.type_in_surname('Nowak')
        add_a_player.type_in_age('01012001')
        add_a_player.type_in_main_position('Goalkeeper')
        add_a_player.wait_for_element_to_be_clickable(add_a_player.submit_button_xpath)
        add_a_player.click_on_the_submit_button()




    @classmethod
    def tearDown(self):
        self.driver.quit()