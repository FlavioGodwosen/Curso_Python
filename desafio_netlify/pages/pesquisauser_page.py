from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PesquisaUserPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='search']")
    
    def search_user(self, username):
        self.wait_for_visible_element(self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.SEARCH_BUTTON).click()