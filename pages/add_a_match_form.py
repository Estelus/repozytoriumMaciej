from pages.base_page import BasePage

class add_a_match_form(BasePage):

    add_language_xpath = "//[@id='__next'],[@class='button']//div[15]"
    add_player_title_xpath = "//*[@id='__next']//div[2]"
    add_email_xpath = "//*[@id='__next']/div[1]/main/div[2]"
    district_xpath = "//[@id='mui-component-select-district']"
    add_link_youtube_button_xpath = "//*[@id='__next']/div[1]/div[2]/div[19]"
    submit_button_xpath = "//*[@id='__next']//ul/li[3]"
    clear_button_xpath = "//span/text('Clear')"
    age_submit_xpath = " //input[@type='MuiInput-formControl']"
    select_leg_xpath = "//*[@id='mui-component-select-leg']"
    surname_xpath = "//div[@name='surname']"

    pass