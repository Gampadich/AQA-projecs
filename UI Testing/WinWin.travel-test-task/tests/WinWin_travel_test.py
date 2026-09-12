import allure
from playwright.sync_api import expect
from actions.adultsSection import AdultsSection
from actions.mainPage import MainPage
from actions.filtersSection import FiltersSection
import re

@allure.feature('Main page testing')
@allure.story('Max Adults section')
@allure.severity(allure.severity_level.CRITICAL)
def test_max_adults(url, page):
    page.goto(url)
    moves = AdultsSection(page)
    mainPage = MainPage(page)
    mainPage.guests_select_button_click()
    counter = moves.plus_button_clicking()
    expect(counter).to_have_value('10')

@allure.feature('Main page testing')
@allure.story('Check Active pets checkboxes')
@allure.severity(allure.severity_level.CRITICAL)
def test_active_pets_checkboxes(url, page):
    page.goto(url)
    mainPage = MainPage(page)
    filtersSection = FiltersSection(page)
    mainPage.filters_button_click()
    filtersSection.see_more_and_checkbox_button_click()
    activeCheckboxes = filtersSection.active_checkboxes_button_click()
    assert len(activeCheckboxes) == 23, f'Checkboxes not active active: {len(activeCheckboxes)}'

@allure.feature('Main page testing')
@allure.story('Check page url after filters')
@allure.severity(allure.severity_level.CRITICAL)
def test_page_url_after_filters(url, page):
    mainPage = MainPage(page)
    page.goto(url)
    cookie_button = page.get_by_role("button", name="Accept all")
    if cookie_button.is_visible():
        cookie_button.click()
        page.wait_for_timeout(300)
    mainPage.click_all_filter_buttons()
    mainPage.click_search_button()
    page.wait_for_url(re.compile(r"search\.filters%5B0%5D\.optionIDs%5B0%5D=2"), timeout=15000)
