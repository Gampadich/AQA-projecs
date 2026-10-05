import pytest
import allure


@pytest.fixture(scope='session')
@allure.step('Provide base application URL')
def url() -> str:
    """Returns the base URL for the SauceDemo web application."""
    return 'https://www.saucedemo.com/'
