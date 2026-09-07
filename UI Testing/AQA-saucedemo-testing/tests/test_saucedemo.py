from playwright.sync_api import expect
from classes.login import LoginPage
from classes.products_page import ProductsPage
import allure

@allure.feature('Авторизація')
@allure.story('Успішний вхід користувача')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_and_visible_title(page, url):
    login_page = LoginPage(page=page, url=url, username='standard_user', password='secret_sauce')
    main_page = ProductsPage(page)
    login_page.login()
    title = main_page.get_title()
    expect(title, message='Title is not visible maybe login data is not correct').to_have_text('Products')

@allure.feature('Сторінка з товарами')
@allure.story('Перевірка найменшої ціни товару на сайті після сортування')
@allure.severity(allure.severity_level.MINOR)
def test_check_first_product_after_sort(page, url):
    login_page = LoginPage(page=page, url=url, username='standard_user', password='secret_sauce')
    main_page = ProductsPage(page)
    login_page.login()
    first_product_price = main_page.sort_and_get_price_of_first_product()
    expect(first_product_price, message='Sort is not working or you have been chosen another option').to_have_text('$7.99')

@allure.feature('Авторизація')
@allure.story('Вхід користувача з неправильними даними')
@allure.severity(allure.severity_level.NORMAL)
def test_negative_login(page, url):
    login_page = LoginPage(page=page, url=url, username='standard_user123', password='secret_sauce132')
    login_page.login()
    error_message = page.locator('h3[data-test="error"]')
    expect(error_message, message='Error message is not visible.').to_be_visible()

@allure.feature('Сторінка з товарами')
@allure.story('Успішна поява товару у кошику')
@allure.severity(allure.severity_level.CRITICAL)
def test_adding_product_to_cart(page, url):
    login_page = LoginPage(page=page, url=url, username='standard_user', password='secret_sauce')
    login_page.login()
    main_page = ProductsPage(page)
    badge = main_page.add_product_to_cart()
    expect(badge, message='Product haven`t added to cart').to_be_visible()
