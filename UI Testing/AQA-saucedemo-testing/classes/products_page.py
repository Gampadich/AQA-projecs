import allure

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title = self.page.locator('.title')
        self.sort = self.page.locator('select[data-test="product-sort-container"]')
        self.item = self.page.locator('.inventory_item_price').first
        self.add_backpack_button = self.page.locator('#add-to-cart-sauce-labs-backpack')
        self.shopping_cart_badge = self.page.locator('span[data-test="shopping-cart-badge"]')

    @allure.step('Перевіряємо наявність заголовку')
    def get_title(self):
        return self.title

    @allure.step('Сортуємо від найнижчої до найвищої ціни товару та беремо ціну товару')
    def sort_and_get_price_of_first_product(self):
        self.sort.select_option('lohi')
        return self.item

    @allure.step('Додаємо товар у кошик')
    def add_product_to_cart(self):
        self.add_backpack_button.click()
        return self.shopping_cart_badge
