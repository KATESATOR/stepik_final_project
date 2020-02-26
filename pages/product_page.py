from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_success_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_text = book_name.text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        success_message_text = success_message.text
        assert book_name_text == success_message_text, "No success message or book name does not match"

    def should_be_actual_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        book_price_text = book_price.text
        total_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        total_price_text = total_price.text
        assert book_price_text == total_price_text, "Total price does not match with book price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                                  "should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                                  "should disappear"
