from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty_check(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTAINS_PRODUCTS), \
            "Items are presented in basket"

    def presence_of_empty_basket_alert(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "No empty basket message"
