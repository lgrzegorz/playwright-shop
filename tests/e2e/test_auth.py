import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.auth
class TestLogin:

    def test_successful_login(self, login_page: LoginPage, credentials: dict):
        """Standard user can log in and reach inventory."""
        login_page.login(
            credentials["standard"]["username"],
            credentials["standard"]["password"],
        )
        assert "inventory" in login_page.get_url()

    def test_locked_user_cannot_login(self, login_page: LoginPage, credentials: dict):
        """Locked-out user sees an error message."""
        login_page.login(
            credentials["locked"]["username"],
            credentials["locked"]["password"],
        )
        assert login_page.is_error_visible()
        assert "locked out" in login_page.get_error_message().lower()

    def test_empty_credentials_show_error(self, login_page: LoginPage):
        """Submitting empty form shows validation error."""
        login_page.login("", "")
        assert login_page.is_error_visible()

    def test_wrong_password_shows_error(self, login_page: LoginPage):
        """Wrong password shows error, user stays on login page."""
        login_page.login("standard_user", "wrong_password")
        assert login_page.is_error_visible()
        assert "inventory" not in login_page.get_url()

    def test_logout(self, inventory_page: InventoryPage):
        """Logged-in user can log out and is redirected to login."""
        inventory_page.logout()
        assert "inventory" not in inventory_page.page.url

