from selenium.webdriver.common.by import By

class MainPageLocators():
    # is a tuple with a pair (a, b)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # is a tuple with a pair (a, b)

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    
    LOGIN_USER_MAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_USER_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "button[name='login_submit']")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_USER_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_USER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_USER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")
