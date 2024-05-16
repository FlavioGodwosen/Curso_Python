from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NomeUserPage(BasePage):
    NAME_HEADER = (By.XPATH, "//h4")
    FOLLOW_LINK = (By.XPATH, "//header/a[text()='follow']")
    
    def username_page(self, username):
        self.wait_for_visible_element(self.NAME_HEADER).send_keys(username)
        self.driver.find_element(*self.FOLLOW_LINK).click()
        
       