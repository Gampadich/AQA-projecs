import pytest
from classes.login import LoginPage
from classes.products_page import ProductsPage


@pytest.fixture
def login_page(page, url):
    """Fixture to provide LoginPage instance."""
    return LoginPage(page=page, url=url, username='standard_user', password='secret_sauce')


@pytest.fixture
def logged_in_page(page, url):
    """Fixture that performs login and returns ProductsPage instance ready for testing."""
    login_pg = LoginPage(page=page, url=url, username='standard_user', password='secret_sauce')
    login_pg.login()
    return ProductsPage(page)
