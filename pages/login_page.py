from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
from .main_page import MainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        page = MainPage(self.browser, self.url)
        page.open()
        page.should_be_login_link()
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        cur_url = self.browser.current_url
        assert "login" in cur_url, f"Substring 'login' is not found in string: {cur_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
