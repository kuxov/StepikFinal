from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BOOK_DESCRIPTION = (By.CSS_SELECTOR, ".product_main :first-child")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert .alertinner strong:first-child")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert .alertinner p:first-child")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p:first-child")
