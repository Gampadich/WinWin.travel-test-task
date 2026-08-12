import allure
from playwright.sync_api import expect
from actions.adultsSection import AdultsSection

@allure.feature('Main page testing')
@allure.story('Max Adults section')
@allure.severity(allure.severity_level.CRITICAL)
def test_max_adults(url, page):
    page.goto(url)
    moves = AdultsSection(page)
    moves.quests_select_button_click()
    counter = moves.plus_button_clicking()
    expect(counter).to_have_value('10')
