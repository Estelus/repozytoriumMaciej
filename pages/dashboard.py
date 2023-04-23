import time

from pages.base_page import BasePage
from selenium import webdriver


class Dashboard(BasePage):
<<<<<<< Updated upstream

    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title



=======
    futbol_kolektyw_logo_xpath = '//*[@title ="Logo Scouts Panel"'
    expected_title = 'Scouts Panel'
    add_player_button_xpath = "//*[@text()='Add player']"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)


>>>>>>> Stashed changes



