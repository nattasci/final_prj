from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "URL doesn't contain 'login' string"
    
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"

        #assert self.is_element_present(*LoginPageLocators.LOGIN_USER_MAIL), "Login user mail field is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_USER_PASSWORD), "Login user password field is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"

        #assert self.is_element_present(*LoginPageLocators.LOGIN_USER_MAIL), "Login user mail field is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_USER_PASSWORD), "Login user password field is not presented"
        #assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is missing"

        #assert self.is_element_present(*LoginPageLocators.REGISTRATION_USER_MAIL), "Registration user mail field is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTRATION_USER_PASSWORD1), "Registration user password1 field is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTRATION_USER_PASSWORD2), "Registration user password2 field is not presented"
        #assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration submit button is not presented"
