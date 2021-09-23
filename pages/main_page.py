from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
