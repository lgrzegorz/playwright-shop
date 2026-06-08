from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for the shopping cart."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.cart_items       = page.locator(".cart_item")
        self.checkout_button  = page.get_by_role("button", name="Checkout")
        self.continue_button  = page.get_by_role("button", name="Continue Shopping")

    def get_item_names(self) -> list[str]:
        return self.cart_items.locator(".inventory_item_name").all_inner_texts()

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def remove_item_by_name(self, name: str) -> None:
        item = self.page.locator(".cart_item", has_text=name)
        item.get_by_role("button", name="Remove").click()

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()
