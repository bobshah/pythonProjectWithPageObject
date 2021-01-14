import pytest
from selenium import webdriver
import allure

from Config.Config import TestData
from PageObjects.LogInPage import LoginPage
from Tests.Test_Base import BaseTest


class Test_Login(BaseTest):

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


    #@allure.description("Validated with invalid username and password")
    def test_with_invalid_login(self):
        """create a object page class"""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.INVALID_USER_NAME, TestData.INVALID_PASSWORD)
        flag = self.loginPage.is_invalid_credentials_error_exist()
        assert flag
        text = self.loginPage.get_invalid_credentials_error()
        assert text == TestData.INVALID_CREDENTIALS_ERROR
