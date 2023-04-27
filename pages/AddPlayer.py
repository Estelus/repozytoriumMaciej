import time

from pages.base_page import BasePage
DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')
class AddAPlayer(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    email_xpath = "//*[@name='email']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    age_xpath = "//*[@name='age']"
    leg_xpath = "//*[@name='leg']"
    club_xpath = "//*[@name='club']"
    level_xpath = "//*[@name='level']"
    main_position_xpath = "//*[@name='mainPosition']"
    second_position_xpath = "//*[@name='secondPosition']"
    achievements_xpath = "//*[@name='achievements']"
    add_language_xpath = "//*[@aria-label='Add language']"
    laczy_nas_pilka_xpath = "//*[@name='webLaczy']"
    dziewiecdziesiat_minut_xpath = "//*[@name='web90']"
    facebook_xpath = "//*[@name='webFB']"
    add_link_to_youtube_xpath = "//*[text()='Add link to Youtube']"
    submit_xpath = "//*[@type='submit']"
    clear_xpath = "//*[text()='Clear']"

    expected_title = "Add player"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    pass
    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_xpath)

    def click_clear_button(self):
        self.click_on_the_element(self.clear_xpath)