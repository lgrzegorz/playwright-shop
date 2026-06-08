from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for https://www.saucedemo.com login screen."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button   = page.get_by_role("button", name="Login")
        self.error_message  = page.locator("[data-test='error']")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        return self.error_message.is_visible()
