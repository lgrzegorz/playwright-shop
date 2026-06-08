from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object covering checkout step one, two and confirmation."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Step one — personal info
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input  = page.get_by_placeholder("Last Name")
        self.zip_input        = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button  = page.get_by_role("button", name="Continue")
        self.error_message    = page.locator("[data-test='error']")
        # Step two — overview
        self.finish_button    = page.get_by_role("button", name="Finish")
        self.summary_subtotal = page.locator(".summary_subtotal_label")
        self.summary_tax      = page.locator(".summary_tax_label")
        self.summary_total    = page.locator(".summary_total_label")
        # Confirmation
        self.confirmation_header = page.locator(".complete-header")

    # ── Step one ──────────────────────────────────────────────────────────────

    def fill_personal_info(self, first: str, last: str, zip_code: str) -> None:
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.zip_input.fill(zip_code)

    def submit_info(self) -> None:
        self.continue_button.click()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    # ── Step two ──────────────────────────────────────────────────────────────

    def get_subtotal(self) -> str:
        return self.summary_subtotal.inner_text()

    def get_total(self) -> str:
        return self.summary_total.inner_text()

    def finish_order(self) -> None:
        self.finish_button.click()

    # ── Confirmation ──────────────────────────────────────────────────────────

    def get_confirmation_text(self) -> str:
        return self.confirmation_header.inner_text()
