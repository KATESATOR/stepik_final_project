from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert "login" in self.browser.current_url, "word 'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "No username field on login page"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "No password field on login page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_USERNAME), "No username field on register page"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "No password field on register page"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM), "No confirm password field on " \
                                                                                      "register page "
