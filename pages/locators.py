from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BOOK_DESCRIPTION = (By.CLASS_NAME, "product_main")
    BOOK_PRICE = (By.CLASS_NAME, "price_color")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    PRICE_MESSAGE = (By.CLASS_NAME, "alert-info")


