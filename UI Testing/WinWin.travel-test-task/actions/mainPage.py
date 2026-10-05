import allure
from playwright.sync_api import Page, Locator


class MainPage:
    """Page Object representing the WinWin Travel Main Page."""

    def __init__(self, page: Page):
        """Initialize MainPage locators and page instance.
        
        :param page: Playwright Page instance
        """
        self.page: Page = page

        # UI Locators
        self.guests_select_button: Locator = page.locator('button[data-wwt-id="guests-select__open--button"]').first
        self.filters_button: Locator = page.locator('button[data-wwt-id="main-search__big-filter-open--button"]').first
        self.recommended_filters_selector: str = 'button[data-wwt-id="main-search__recommended-filter--button"]'

    @allure.step('Open guests selection dropdown')
    def open_guests_selection(self) -> None:
        """Clicks the button to open guests selection popover."""
        self.guests_select_button.click()

    @allure.step('Open main filters modal/drawer')
    def open_filters(self) -> None:
        """Clicks the main filter button to display all available filters."""
        self.filters_button.click()

    @allure.step('Click all recommended filter tags on the main page')
    def click_all_recommended_filters(self) -> None:
        """Finds all visible recommended filter buttons and clicks them iteratively."""
        recommended_buttons = self.page.locator(self.recommended_filters_selector)
        
        # Wait for the first recommended tag to be visible
        recommended_buttons.first.wait_for(state="visible", timeout=10000)
        
        count = recommended_buttons.count()
        for index in range(count):
            recommended_buttons.nth(index).click()

    @allure.step('Execute search action')
    def click_search_button(self) -> None:
        """Dismisses active popups/modals and navigates to the search results page."""
        # Close open dropdowns/modals via ESC key
        self.page.keyboard.press("Escape")
        
        search_link = self.page.get_by_role("link", name="Search").first
        search_link.wait_for(state="visible", timeout=5000)
        
        href = search_link.get_attribute("href")
        if href:
            target_url = href if href.startswith("http") else f"https://winwin.travel{href}"
            self.page.goto(target_url)
        else:
            search_link.click()
