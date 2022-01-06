from selenium.webdriver.common.by import By

class BasePageLocators():
     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
     LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")

    PRODUCT_NAME_IN_MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")

class MainPageLocators():
    pass
