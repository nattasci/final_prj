from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LOOKUP_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

     
class BasketPageLocators():  
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, ".content p")
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, ".basket-title")

    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_USER_MAIL = (By.CSS_SELECTOR, " #id_registration-email") 
    REGISTRATION_USER_PASSWORD1 = (By.CSS_SELECTOR, " #id_registration-password1")
    REGISTRATION_USER_PASSWORD2 = (By.CSS_SELECTOR, " #id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, ".btn-primary[name='registration_submit']")

    
class MainPageLocators():
    pass


class ProductPageLocators():    
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")

    PRODUCT_NAME_IN_MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")
