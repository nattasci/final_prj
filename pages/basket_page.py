from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), "Basket is not empty, but should be"

    def should_be_text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Basket is empty message is missing"
