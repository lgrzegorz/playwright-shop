from playwright.sync_api import Page, Locator


class BasePage:
    """Base class for all Page Objects."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def wait_for_page_load(self) -> None:
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url
