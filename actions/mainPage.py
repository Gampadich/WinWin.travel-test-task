import allure

class MainPage:
    def __init__(self, page):
        self.page = page
        self.guests_select_button = page.locator('button[data-wwt-id="guests-select__open--button"]').first
        self.filtersButton = page.locator('button[data-wwt-id="main-search__big-filter-open--button"]').first

    @allure.step('Clicking quests select button')
    def guests_select_button_click(self):
        return self.guests_select_button.click()

    @allure.step('Clicking filters button')
    def filters_button_click(self):
        return self.filtersButton.click()
