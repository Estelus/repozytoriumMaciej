from pages.base_page import BasePage

class Dashboard(BasePage):
    logo_scouts_panel_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[1]"
    add_player_button_xpath = '//a[contains(button )]'
    dev_team_contact_xpath = "//a//span MuiButton-label"
    scouts_panel_title_xpath = "//[@id='__next']//h2"
    activity_xpath = "//*[id='__next']/div[3]div[3]/div/div/h2"
    last_created_player_button_xpath = "//*([@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1])"
    header_button_xpath = "//(div[@class='header'])"
    player_count_xpath = "//(div[@name='Players count'])"
    last_updated_player_xpath = "//*([id=__next]/main/div[3]/div[3]/div/div/a[11]/button/span.MuiButton-label)"
    event_count_tab_xpath = "//*([@id='__next']/div[1]/main/div[2]/div[4]/div)"

    pass



