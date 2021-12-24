from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_compare_prices()
    page.should_compare_names()




