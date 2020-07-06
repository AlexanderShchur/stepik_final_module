from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_book_name(self):
        title = self.browser.find_element(*ProductPageLocators.FIND_BOOK_NAME)
        book_name = title.text
        return book_name

    def get_book_name_from_basket_alert_message(self):
        alert_message = self.browser.find_element(*ProductPageLocators.FIND_BOOK_NAME_FROM_ALERT_MESSAGE)
        alert_message = alert_message.text
        return alert_message

    def get_price_on_basket_alert(self):
        price = self.browser.find_element(*ProductPageLocators.GET_PRICE_ON_BASKET_ALERT)
        price = price.text
        return price

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.GET_PRODUCT_PRICE)
        product_price = product_price.text
        return product_price

    def equal_price(self, price):
        assert self.get_price_on_basket_alert() == price

    def equal_book_name(self, book_name):
        assert self.get_book_name_from_basket_alert_message() == book_name

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        add_button.click()
        self.solve_quiz_and_get_code()

    def add_to_basket_without_quiz(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_FORM)
        add_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"
