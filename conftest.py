import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, BrowserContext
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

load_dotenv()


# ── Config ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="session")
def credentials() -> dict:
    return {
        "standard": {
            "username": os.getenv("STANDARD_USER", "standard_user"),
            "password": os.getenv("PASSWORD", "secret_sauce"),
        },
        "locked": {
            "username": os.getenv("LOCKED_USER", "locked_out_user"),
            "password": os.getenv("PASSWORD", "secret_sauce"),
        },
    }


# ── Browser options ──────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "record_video_dir": None,
    }


# ── Page Object fixtures ─────────────────────────────────────────────────────

@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    page.goto(base_url)
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page, base_url: str, credentials: dict) -> InventoryPage:
    """Returns InventoryPage already logged in as standard user."""
    login = LoginPage(page)
    page.goto(base_url)
    login.login(credentials["standard"]["username"], credentials["standard"]["password"])
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page, base_url: str, credentials: dict) -> CartPage:
    """Returns CartPage with one item already added."""
    login = LoginPage(page)
    page.goto(base_url)
    login.login(credentials["standard"]["username"], credentials["standard"]["password"])
    inv = InventoryPage(page)
    inv.add_item_to_cart_by_index(0)
    inv.go_to_cart()
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page, base_url: str, credentials: dict) -> CheckoutPage:
    """Returns CheckoutPage step-one with item in cart."""
    login = LoginPage(page)
    page.goto(base_url)
    login.login(credentials["standard"]["username"], credentials["standard"]["password"])
    inv = InventoryPage(page)
    inv.add_item_to_cart_by_index(0)
    inv.go_to_cart()
    cart = CartPage(page)
    cart.proceed_to_checkout()
    return CheckoutPage(page)


@pytest.fixture
def fresh_inventory_page(page: Page, base_url: str, credentials: dict) -> InventoryPage:
    """Fresh login every time — used for sorting tests to avoid stale state."""
    page.goto(base_url)
    login = LoginPage(page)
    login.login(credentials["standard"]["username"], credentials["standard"]["password"])
    page.wait_for_url("**/inventory.html")
    return InventoryPage(page)
