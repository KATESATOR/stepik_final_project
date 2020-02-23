from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        # self.should_be_promo_url()
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.should_be_actual_price()

    # def should_be_promo_url(self):
    #     assert "?promo=newYear" in self.browser.current_url, "parameter '?promo=newYear' not in current url"

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


