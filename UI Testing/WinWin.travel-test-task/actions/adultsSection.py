import allure
from playwright.sync_api import Page, Locator


class AdultsSection:
    """Component representing the Adults Counter selector in booking forms."""

    def __init__(self, page: Page):
        """Initialize AdultsSection elements.
        
        :param page: Playwright Page instance
        """
        self.page: Page = page

        # UI Locators
        self.counter_plus_button: Locator = page.locator(
            'button[data-wwt-id="number-counter__plus--button"]'
        ).first
        self.counter_input: Locator = page.locator(
            'input[data-wwt-id="number-counter__input--input"]'
        ).first

    @allure.step('Click increment adult button until maximum threshold is reached')
    def increment_adults_to_maximum(self) -> Locator:
        """Clicks the plus button iteratively until it becomes disabled.
        
        :return: Locator for the counter input field
        """
        while self.counter_plus_button.is_enabled():
            self.counter_plus_button.click()
            # Wait briefly for UI state transition if necessary

        return self.counter_input

    @allure.step('Get current adult passengers count')
    def get_adults_count(self) -> int:
        """Extracts and converts the current input value to an integer."""
        count_value = self.counter_input.get_attribute('value') or '0'
        return int(count_value)
