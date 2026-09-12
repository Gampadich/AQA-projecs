import allure

class FiltersSection:
    def __init__(self, page):
        self.page = page
        self.see_more_button = page.locator('button[data-wwt-id="filter__see-more--button"]').first
        self.pets_checkbox_button = page.locator('button[data-wwt-id="filter-11__title--checkbox"]').first
        self.activeCheckboxesSelector = 'button[data-wwt-id="filter__option--checkbox"][aria-checked="true"]'

    @allure.step('Clicking see_more_button and pets checkbox button')
    def see_more_and_checkbox_button_click(self):
        self.page.wait_for_timeout(1000)
        see_more = self.page.locator('button[data-wwt-id="filter__see-more--button"]').first
        if see_more.is_visible():
            see_more.click()
            self.page.wait_for_timeout(500)
        pets_btn = self.pets_checkbox_button
        pets_btn.wait_for(state="visible", timeout=10000)
        pets_btn.scroll_into_view_if_needed()
        pets_btn.click()
        self.page.wait_for_selector(self.activeCheckboxesSelector, state="attached", timeout=5000)

    @allure.step('Checking active checkboxes button')
    def active_checkboxes_button_click(self):
        return self.page.locator(self.activeCheckboxesSelector).all()