import time

from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')

class Dashboard(BasePage):
    scouts_panel_title_xpath = "//header/div/h6"
    main_page_button_xpath = "//span[text()='Main page']//ancestor-or-self::div[@role='button']"
    players_button_xpath = "//ul[1]/div[2]"
    change_language_button_xpath = "//*/ul[2]/div[1]"
    sign_out_button_xpath = "//span[text()='Sign out']//ancestor-or-self::div[@role='button']"
    add_player_button_xpath = "//*[2][name() = 'a']/button"
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    dev_team_contact_button_xpath = "//a[@target='_blank']"
    logo_scouts_panel_xpath = "//div[@title='Logo Scouts Panel']"
    players_count_section_xpath = "//div[text()='Players count']/parent::div/parent::div"
    matches_count_section_xpath = "// div[text() = 'Matches count'] / parent::div / parent::div"
    reports_count_section_xpath = "//div[text()='Reports count']/parent::div/parent::div"
    polish_language_xpath = "//*[text()='Polski']"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"



    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    def click_add_a_player_button(self):
        self.click_on_the_element(self.add_player_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_polish_button(self):
        self.click_on_the_element(self.polish_language_xpath)

    def click_players_button(self):
        self.click_on_the_element(self.players_button_xpath)