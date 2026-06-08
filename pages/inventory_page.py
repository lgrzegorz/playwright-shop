from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for the product listing page."""

    URL_SUFFIX = "/inventory.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_title       = page.locator(".title")
        self.inventory_items  = page.locator(".inventory_item")
        self.cart_badge       = page.locator(".shopping_cart_badge")
        self.cart_link        = page.locator(".shopping_cart_link")
        self.sort_dropdown    = page.locator("[data-test='product_sort_container']")
        self.burger_menu      = page.get_by_role("button", name="Open Menu")
        self.logout_link      = page.locator("#logout_sidebar_link")

    # ── Navigation ────────────────────────────────────────────────────────────

    def go_to_cart(self) -> None:
        self.cart_link.click()

    def logout(self) -> None:
        self.burger_menu.click()
        self.logout_link.click()

    # ── Products ──────────────────────────────────────────────────────────────

    def get_item_names(self) -> list[str]:
        return self.inventory_items.locator(".inventory_item_name").all_inner_texts()

    def get_item_prices(self) -> list[str]:
        return self.inventory_items.locator(".inventory_item_price").all_inner_texts()

    def get_item_count(self) -> int:
        return self.inventory_items.count()

    def add_item_to_cart_by_index(self, index: int) -> str:
        """Adds item at given index to cart. Returns item name."""
        item = self.inventory_items.nth(index)
        item.get_by_role("button", name="Add to cart").click()
        return item.locator(".inventory_item_name").inner_text()

    def add_item_to_cart_by_name(self, name: str) -> None:
        item = self.page.locator(".inventory_item", has_text=name)
        item.get_by_role("button", name="Add to cart").click()

    def get_cart_badge_count(self) -> int:
        if not self.cart_badge.is_visible():
            return 0
        return int(self.cart_badge.inner_text())

    # ── Sorting ───────────────────────────────────────────────────────────────

    def sort_by(self, option: str) -> None:
        """Options: 'az', 'za', 'lohi', 'hilo'"""
        self.sort_dropdown.select_option(option)
