from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Config.Config import TestData
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    """By locators """
    EMAIL = (By.NAME, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.CLASS_NAME, "button")
    INVALID_CREDENTIALS_TXT = (By.XPATH, "//span[contains(text(),'Invalid credentials')]")

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

    def is_invalid_credentials_error_exist(self):
        return self.is_visiable(self.INVALID_CREDENTIALS_TXT)

    """get text"""
    def get_invalid_credentials_error(self):
        return self.get_element_text(self.INVALID_CREDENTIALS_TXT)

    """this is used to login to app"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
