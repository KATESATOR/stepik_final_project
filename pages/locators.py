from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "//input[@id='id_login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "//input[@id='id_login-password']")
    REGISTER_USERNAME = (By.CSS_SELECTOR, "//input[@id='id_registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "//input[@id='id_registration-password1']")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "//input[@id='id_registration-password2']")

