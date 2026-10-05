import allure
from playwright.sync_api import Page, Locator


class FiltersSection:
    """Component representing the Filters section on search/listing pages."""

    def __init__(self, page: Page):
        """Initialize FiltersSection elements.
        
        :param page: Playwright Page instance
        """
        self.page: Page = page

        # UI Locators
        self.see_more_button: Locator = page.locator('button[data-wwt-id="filter__see-more--button"]').first
        self.pets_checkbox_button: Locator = page.locator('button[data-wwt-id="filter-11__title--checkbox"]').first
        self.active_checkboxes_selector: str = 'button[data-wwt-id="filter__option--checkbox"][aria-checked="true"]'

    @allure.step('Expand filters list and enable "Pets allowed" checkbox')
    def select_pets_filter(self) -> None:
        """Expands hidden filter options if needed and toggles the pets checkbox."""
        # Click "See More" if present
        if self.see_more_button.is_visible():
            self.see_more_button.click()

        # Ensure pets checkbox is ready, scroll and click
        self.pets_checkbox_button.wait_for(state="visible", timeout=10000)
        self.pets_checkbox_button.scroll_into_view_if_needed()
        self.pets_checkbox_button.click()

        # Wait until at least one active checkbox is rendered in the DOM
        self.page.wait_for_selector(self.active_checkboxes_selector, state="attached", timeout=5000)

    @allure.step('Get active/checked filter checkboxes')
    def get_active_checkboxes(self) -> Locator:
        """Returns the Locator for all currently checked/active filter options.
        
        :return: Playwright Locator matching all checked checkboxes
        """
        return self.page.locator(self.active_checkboxes_selector)
