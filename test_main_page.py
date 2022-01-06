import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip(reason="I am testing something different now")
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip(reason="I am testing something different now")    
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link) # Гость открывает главную страницу
    page.open()
    page.go_to_basket_page()# Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty() # Ожидаем, что в корзине нет товаров
    basket_page.should_be_text_basket_empty() # Ожидаем, что есть текст о том что корзина пуста

