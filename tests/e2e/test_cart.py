import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.cart
class TestCart:

    def test_added_item_appears_in_cart(
        self, inventory_page: InventoryPage
    ):
        """Item added on inventory page appears in the cart."""
        name = inventory_page.add_item_to_cart_by_index(0)
        inventory_page.go_to_cart()
        cart = CartPage(inventory_page.page)
        assert name in cart.get_item_names()

    def test_cart_shows_correct_item_count(
        self, inventory_page: InventoryPage
    ):
        """Cart contains the same number of items that were added."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.add_item_to_cart_by_index(1)
        inventory_page.go_to_cart()
        cart = CartPage(inventory_page.page)
        assert cart.get_item_count() == 2


@pytest.mark.regression
@pytest.mark.cart
class TestCartRemoval:

    def test_remove_item_from_cart(self, cart_page: CartPage):
        """Removing an item empties the cart."""
        names = cart_page.get_item_names()
        cart_page.remove_item_by_name(names[0])
        assert cart_page.get_item_count() == 0
