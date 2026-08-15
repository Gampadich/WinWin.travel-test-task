import allure

class MainPage:
    def __init__(self, page):
        self.page = page
        self.guests_select_button = page.locator('button[data-wwt-id="guests-select__open--button"]').first
        self.filtersButton = page.locator('button[data-wwt-id="main-search__big-filter-open--button"]').first
        self.recommended_filters_buttons = 'button[data-wwt-id="main-search__recommended-filter--button"]'

    @allure.step('Clicking quests select button')
    def guests_select_button_click(self):
        return self.guests_select_button.click()

    @allure.step('Clicking filters button')
    def filters_button_click(self):
        return self.filtersButton.click()

    @allure.step('Clicking all recommended filters buttons on main page')
    def click_all_filter_buttons(self):
        recommended_filters = self.page.query_selector_all(self.recommended_filters_buttons)
        recommended_filters[0].click()
        recommended_filters[1].click()
        recommended_filters[2].click()
        recommended_filters[3].click()
        recommended_filters[4].click()

    @allure.step('Click search button')
    def click_search_button(self):
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(300)
        search_link = self.page.get_by_role("link", name="Search").first
        href = search_link.get_attribute("href")
        self.page.goto(f"https://winwin.travel{href}")
