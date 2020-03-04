from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert "login" in self.browser.current_url, "word 'login' not in current url"

    def should_be_login_form(self):
        # Проверка, что есть форма логина на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "No username field on login page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "No password field on login page"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_USERNAME), "No username field on register page"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "No password field on register page"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM), "No confirm password field on " \
                                                                                      "register page "

    def register_new_user(self):
        # Регистрация пользователя
        email = str(time.time()) + "@fakemail.org"
        password = str(int(time.time()))
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_USERNAME)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)
        password_field_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_field_confirm.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
