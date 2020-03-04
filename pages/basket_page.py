from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    # Проверка что корзина пустая
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Item is present, but should not be"

    # Проверка что есть сообщение о пустой корзине
    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        basket_message_text = basket_message.text
        assert "Your basket is empty. Continue shopping" == basket_message_text, "Basket is not empty, but should be"
