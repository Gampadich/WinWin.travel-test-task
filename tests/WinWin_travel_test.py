import allure
from playwright.sync_api import expect
from actions.adultsSection import AdultsSection
from actions.mainPage import MainPage
from actions.filtersSection import FiltersSection

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
    assert len(activeCheckboxes) == 23, f'Checkboxes not active active: {activeCheckboxes}'
