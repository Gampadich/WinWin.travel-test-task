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

        # 1. Розгортаємо список ("Дивитися більше"), якщо кнопка є
        if self.see_more_button.is_visible():
            self.see_more_button.click(force=True)
            self.page.wait_for_timeout(500)

        # 2. Натискаємо на головну кнопку чекбоксу тварин (звертаємося до правильної змінної)
        self.pets_checkbox_button.wait_for(state="visible", timeout=10000)
        self.pets_checkbox_button.click(force=True)

    @allure.step('Checking active checkboxes button')
    def active_checkboxes_button_click(self):
        # Очікуємо оновлення DOM після кліку
        self.page.wait_for_timeout(1000)

        # Використовуємо твій точний селектор для активних чекбоксів
        active_elements = self.page.locator(self.activeCheckboxesSelector).all()

        return active_elements