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
        see_more = self.page.locator("button[data-wwt-id='filter__see-more--button']").first
        if see_more.is_visible():
            see_more.click(force=True)
            self.page.wait_for_timeout(500)
        if hasattr(self, 'pets_checkbox'):
            self.pets_checkbox.click(force=True)

    @allure.step('Checking active checkboxes button')
    def active_checkboxes_button_click(self):
        self.page.wait_for_timeout(1000)
        self.page.query_selector_all(self.activeCheckboxesSelector)
