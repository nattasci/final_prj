from selenium.webdriver.common.by import By

class MainPageLocators():

    # each locator is represented by a pair (a, b), where "a" is how to look and "b" what to look for
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
