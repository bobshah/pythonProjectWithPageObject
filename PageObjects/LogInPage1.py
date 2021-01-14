from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Config.Config import TestData
from PageObjects.BasePage import BasePage

class LoginPage(BasePage):

    """By locators """
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    """Create a constructor, super keyword to call parent class constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        WebDriverWait(self.driver, 10)

    """page actions"""
    """This is used to get page title"""
    def get_login_title(self, title):
        return self.get_title(title)

    """this is used to check sign up link"""
    def is_signup_link_exist(self):
        return self.is_visiable(self.SIGNUP_LINK)

    """this is used to login to app"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)


