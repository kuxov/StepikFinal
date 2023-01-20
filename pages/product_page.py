from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_correct_success_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_DESCRIPTION)
        msg_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)

        book_name_value = book_name.get_attribute("h1")
        msg_name_value = msg_name.get_attribute("strong")

        assert (book_name_value, msg_name_value), "book title message does not match actual title"

    def should_be_correct_price_message(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        msg_cart = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)

        book_price_value = book_price.text
        msg_cart_value = msg_cart.get_attribute("strong")

        assert (book_price_value, msg_cart_value), "price message does not match actual price"
