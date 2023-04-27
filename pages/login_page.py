import time

from pages.base_page import BasePage

DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')
class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    scouts_panel_title_xpath = "//div[@class='MuiCardContent-root']//h5"
    listbox_language_xpath = "//div[@aria-haspopup='listbox']"
    remind_password_hyperlink_xpath = "//a [text()='Remind password']"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/login" #

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)


    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)


    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.login_url) == self.expected_title

