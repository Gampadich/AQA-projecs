import re
import allure
from playwright.sync_api import expect
from actions.adultsSection import AdultsSection
from actions.mainPage import MainPage
from actions.filtersSection import FiltersSection


@allure.feature("Main Page Functionality")
class TestMainPage:

    @allure.story("Maximum Adults Selection Limit")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_max_adults(self, url, page):
        page.goto(url)
        adults_section = AdultsSection(page)
        main_page = MainPage(page)

        main_page.guests_select_button_click()
        counter = adults_section.plus_button_clicking()

        expect(
            counter, 
            message="Adults counter did not reach expected maximum value of 10"
        ).to_have_value("10")

    @allure.story("Check Active Pets Filter Checkboxes")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_active_pets_checkboxes(self, url, page):
        page.goto(url)
        main_page = MainPage(page)
        filters_section = FiltersSection(page)

        main_page.filters_button_click()
        filters_section.see_more_and_checkbox_button_click()
        
        # Використовуємо Locator замість списку Python для підтримки auto-retry в Playwright
        active_checkboxes_locator = filters_section.get_active_checkboxes() if hasattr(filters_section, 'get_active_checkboxes') else page.locator(filters_section.activeCheckboxesSelector)
        
        expect(
            active_checkboxes_locator, 
            message="Active checkboxes count mismatch after applying pets filter"
        ).to_have_count(23)

    @allure.story("Verify Target URL Parameters After Filter Submission")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page_url_after_filters(self, url, page):
        main_page = MainPage(page)
        page.goto(url)

        # Gracefully accept cookies if present
        cookie_button = page.get_by_role("button", name="Accept all")
        if cookie_button.is_visible():
            cookie_button.click()

        main_page.click_all_filter_buttons()
        main_page.click_search_button()

        # Verify URL structure contains expected filter options in query params
        expect(page).to_have_url(
            re.compile(r"search\.filters%5B0%5D\.optionIDs%5B0%5D=2"), 
            timeout=15000
        )
