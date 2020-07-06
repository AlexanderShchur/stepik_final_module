from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    FIND_BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    FIND_BOOK_NAME_FROM_ALERT_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    GET_PRICE_ON_BASKET_ALERT = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    GET_PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
