import pytest
from pages.inventory_page import InventoryPage
from utils.helpers import parse_price


@pytest.mark.smoke
class TestInventory:

    def test_inventory_page_loads(self, inventory_page: InventoryPage):
        """Inventory page shows the correct title."""
        assert inventory_page.page_title.inner_text() == "Products"

    def test_inventory_shows_six_products(self, inventory_page: InventoryPage):
        """Default inventory contains exactly 6 products."""
        assert inventory_page.get_item_count() == 6

    def test_all_products_have_prices(self, inventory_page: InventoryPage):
        """Every product has a visible price."""
        prices = inventory_page.get_item_prices()
        assert len(prices) == 6
        for price in prices:
            assert "$" in price

    def test_add_single_item_updates_badge(self, inventory_page: InventoryPage):
        """Cart badge shows 1 after adding one item."""
        inventory_page.add_item_to_cart_by_index(0)
        assert inventory_page.get_cart_badge_count() == 1

    def test_add_multiple_items_updates_badge(self, inventory_page: InventoryPage):
        """Cart badge reflects correct count after adding multiple items."""
        inventory_page.add_item_to_cart_by_index(0)
        inventory_page.add_item_to_cart_by_index(1)
        inventory_page.add_item_to_cart_by_index(2)
        assert inventory_page.get_cart_badge_count() == 3


@pytest.mark.regression
class TestSorting:

    def test_sort_by_name_az(self, inventory_page: InventoryPage):
        """Products sorted A→Z are in ascending alphabetical order."""
        inventory_page.sort_by("az")
        names = inventory_page.get_item_names()
        assert names == sorted(names)

    def test_sort_by_name_za(self, inventory_page: InventoryPage):
        """Products sorted Z→A are in descending alphabetical order."""
        inventory_page.sort_by("za")
        names = inventory_page.get_item_names()
        assert names == sorted(names, reverse=True)

    def test_sort_by_price_low_to_high(self, inventory_page: InventoryPage):
        """Products sorted by price low→high are in ascending price order."""
        inventory_page.sort_by("lohi")
        prices = [parse_price(p) for p in inventory_page.get_item_prices()]
        assert prices == sorted(prices)

    def test_sort_by_price_high_to_low(self, inventory_page: InventoryPage):
        """Products sorted by price high→low are in descending price order."""
        inventory_page.sort_by("hilo")
        prices = [parse_price(p) for p in inventory_page.get_item_prices()]
        assert prices == sorted(prices, reverse=True)
