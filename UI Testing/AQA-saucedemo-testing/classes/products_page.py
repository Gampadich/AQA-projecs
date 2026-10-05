import allure
from playwright.sync_api import Page, Locator


class ProductsPage:
    """Page Object representing the Products/Inventory page of SauceDemo."""

    def __init__(self, page: Page):
        """Initialize Products Page elements and driver.
        
        :param page: Playwright Page instance
        """
        self.page: Page = page

        # UI Locators
        self.title_heading: Locator = self.page.locator('.title')
        self.sort_dropdown: Locator = self.page.locator('select[data-test="product-sort-container"]')
        self.inventory_item_prices: Locator = self.page.locator('.inventory_item_price')
        self.add_backpack_button: Locator = self.page.locator('#add-to-cart-sauce-labs-backpack')
        self.shopping_cart_badge: Locator = self.page.locator('span[data-test="shopping-cart-badge"]')

    @allure.step("Get page title text")
    def get_title_text(self) -> str:
        """Returns the inner text of the main page title."""
        return self.title_heading.inner_text()

    @allure.step("Sort products by option and get first item price")
    def sort_and_get_first_product_price(self, sort_option: str = "lohi") -> str:
        """Sorts the inventory list and returns the price text of the first item.
        
        :param sort_option: Sort option code ('az', 'za', 'lohi', 'hilo')
        :return: Price string of the top product (e.g., '$7.99')
        """
        self.sort_dropdown.select_option(sort_option)
        return self.inventory_item_prices.first.inner_text()

    @allure.step("Add Sauce Labs Backpack to cart")
    def add_backpack_to_cart(self) -> None:
        """Clicks the 'Add to cart' button for the Sauce Labs Backpack."""
        self.add_backpack_button.click()

    @allure.step("Get total items count from shopping cart badge")
    def get_cart_badge_count(self) -> int:
        """Returns the numeric count shown on the cart icon badge."""
        if self.shopping_cart_badge.is_visible():
            return int(self.shopping_cart_badge.inner_text())
        return 0
