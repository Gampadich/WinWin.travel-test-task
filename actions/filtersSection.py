import allure

class FiltersSection:
    def __init__(self, page):
        self.page = page
        self.see_more_button = page.locator('button[data-wwt-id="filter__see-more--button"]').first
        self.pets_checkbox_button = page.locator('button[data-wwt-id="filter-11__title--checkbox"]').first
        self.activeCheckboxesSelector = 'button[data-wwt-id="filter__option--checkbox"][aria-checked="true"]'

    @allure.step('Clicking see_more_button and pets checkbox button')
    def see_more_and_checkbox_button_click(self):
        self.see_more_button.wait_for(state="visible", timeout=10000)
        self.see_more_button.scroll_into_view_if_needed()
        self.see_more_button.click()

    @allure.step('Checking active checkboxes button')
    def active_checkboxes_button_click(self):
        return self.page.query_selector_all(self.activeCheckboxesSelector)
