from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
<<<<<<< Updated upstream
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    login_url = ("https://scouts-test.futbolkolektyw.pl/en/")
    expected_title = 'Scouts panel - sign in'
    title_of_the_box_xpath = "//*[@id='next']/form/div/div[1]/h5"
    header_of_the_box = 'Scouts Panel'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_the_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
=======
    password_field_xpath = "//*([@id='password-label'])"
    sign_in_button_xpath = "//input[@type='submit']"
    login_page_title = '//*[@class="title"]'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def title_of_page(self,title):
        self.title_of_page(self.login_page_title, title)
>>>>>>> Stashed changes
