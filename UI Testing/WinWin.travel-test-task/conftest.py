from typing import Dict, Any
import pytest
import allure
from playwright.sync_api import Page
from actions.mainPage import MainPage
from actions.adultsSection import AdultsSection
from actions.filtersSection import FiltersSection


@pytest.fixture(scope="session")
@allure.step("Provide base application URL")
def url() -> str:
    """Returns the base URL for the WinWin Travel application."""
    return "https://winwin.travel/"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: Dict[str, Any]) -> Dict[str, Any]:
    """Configures global browser context settings such as viewport resolution."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


# Optional: Page Object Fixtures to clean up test code boilerplate
@pytest.fixture
def main_page(page: Page) -> MainPage:
    """Provides an initialized MainPage instance."""
    return MainPage(page)


@pytest.fixture
def adults_section(page: Page) -> AdultsSection:
    """Provides an initialized AdultsSection instance."""
    return AdultsSection(page)


@pytest.fixture
def filters_section(page: Page) -> FiltersSection:
    """Provides an initialized FiltersSection instance."""
    return FiltersSection(page)
