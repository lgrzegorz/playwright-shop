import pytest
from pages.checkout_page import CheckoutPage
from utils.helpers import generate_customer, parse_price


@pytest.mark.smoke
@pytest.mark.checkout
class TestCheckoutHappyPath:

    def test_complete_checkout_flow(self, checkout_page: CheckoutPage):
        """Full happy-path: fill info → overview → confirm order."""
        customer = generate_customer()
        checkout_page.fill_personal_info(
            customer["first_name"],
            customer["last_name"],
            customer["zip_code"],
        )
        checkout_page.submit_info()
        # Step two — verify overview loaded
        assert "checkout-step-two" in checkout_page.get_url()
        checkout_page.finish_order()
        # Confirmation
        assert "Thank you" in checkout_page.get_confirmation_text()

    def test_order_total_is_present(self, checkout_page: CheckoutPage):
        """Checkout overview shows a non-zero total."""
        customer = generate_customer()
        checkout_page.fill_personal_info(
            customer["first_name"],
            customer["last_name"],
            customer["zip_code"],
        )
        checkout_page.submit_info()
        total_text = checkout_page.get_total()
        total = parse_price(total_text.split("$")[-1])
        assert total > 0


@pytest.mark.regression
@pytest.mark.checkout
class TestCheckoutValidation:

    def test_empty_first_name_shows_error(self, checkout_page: CheckoutPage):
        """Submitting without first name shows validation error."""
        checkout_page.fill_personal_info("", "Doe", "12345")
        checkout_page.submit_info()
        assert checkout_page.get_error_message() != ""

    def test_empty_last_name_shows_error(self, checkout_page: CheckoutPage):
        """Submitting without last name shows validation error."""
        checkout_page.fill_personal_info("John", "", "12345")
        checkout_page.submit_info()
        assert checkout_page.get_error_message() != ""

    def test_empty_zip_shows_error(self, checkout_page: CheckoutPage):
        """Submitting without zip code shows validation error."""
        checkout_page.fill_personal_info("John", "Doe", "")
        checkout_page.submit_info()
        assert checkout_page.get_error_message() != ""
