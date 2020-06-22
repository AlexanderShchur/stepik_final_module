import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    book_name = page.get_book_name()
    page.add_to_basket()
    # assert book_name == page.get_book_name_from_basket_alert_message()
    page.equal_book_name(book_name)
    # assert page.get_price_on_basket_alert() == page.get_product_price()
    page.equal_price(page.get_product_price())