from pages.base_page import BasePage
from pages.locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):

    def cart_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def message_of_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT)


