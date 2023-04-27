from pages.base_page import BasePage
DRIVER_PATH = ('C:\TestFiles\chromedriver.exe')

class MatchForm(BasePage):
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//span[text()='Clear']//parent::button"
    player_button_xpath = "//ul[2]/div[1]"
    matches_button_xpath = "//span[text()='Matches']/ancestor::div[2]"
    reports_button_xpath = "//span[text()='Reports']/ancestor::div[2]"
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    date_selection_xpath = "//input[@name='date']"

    pass