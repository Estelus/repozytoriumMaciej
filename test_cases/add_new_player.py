import os
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.AddPlayer import AddPlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')

class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
        self.driver.get("https://scouts.futbolkolektyw.pl/en")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


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