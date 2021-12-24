from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
   
    def should_be_product_page(self):
        self.should_be_promo_in_url
        self.should_be_product_name()
        self.should_be_product_price()
        
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is missing"
    
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is missing"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is missing"

    def should_be_promo_in_url(self):
        assert "promo=NewYear" in self.browser.current_url, "New year promo is missing in url"

    def should_compare_prices(self):
        p_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert p_price == basket_price, "Product price and basket price are not equal"

    def should_compare_names(self):
        p_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        msg = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert p_name in msg, "The product name is not in the message"

    def should_add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        
