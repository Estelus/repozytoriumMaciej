import os
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.remind_password_page import RemindPasswordPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.base_page import BasePage
DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')


class RemindPasswordPage(BasePage):
    remind_pw_form_title_xpath = "//h5"
    remind_pw_form_title_text = "Remind password"
    email_field_xpath = "//*[@name='email']"
    send_button_xpath = "//*[@type='submit']"
    remind_pw_page_url = "https://scouts-test.futbolkolektyw.pl/en/remind"
    expected_title = 'Remind password'

    def title_of_the_page(self):
        assert self.get_page_title == self.expected_title
