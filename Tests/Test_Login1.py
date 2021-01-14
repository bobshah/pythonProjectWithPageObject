import pytest
from selenium import webdriver

from Config.Config import TestData
from PageObjects.LogInPage import LoginPage
from Tests.Test_Base import BaseTest


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loninPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        """create a object page class"""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    # @allure.description("Validated page title")
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    # @allure.description("Validated with valid username and password")
    def test_login(self):
        """create a object page class"""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
