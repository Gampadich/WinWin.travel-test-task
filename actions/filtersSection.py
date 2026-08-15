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

        # 1. Розгортаємо "Дивитися більше", якщо кнопка є
        see_more = self.page.locator('button[data-wwt-id="filter__see-more--button"]').first
        if see_more.is_visible():
            see_more.click(force=True)
            self.page.wait_for_timeout(500)

        # 2. Шукаємо чекбокс тварин за атрибутом або текстом
        pets_btn = self.pets_checkbox_button

        # Якщо за замовчуванням за id="filter-11..." не знайдено, шукаємо за текстом або загальним атрибутом
        if not pets_btn.is_visible():
            pets_btn = self.page.locator("button[data-wwt-id*='title--checkbox']").first

        # 3. Клікаємо з force=True
        pets_btn.click(force=True)

    @allure.step('Checking active checkboxes button')
    def active_checkboxes_button_click(self):
        # Очікуємо оновлення DOM після кліку
        self.page.wait_for_timeout(1000)

        # Використовуємо твій точний селектор для активних чекбоксів
        active_elements = self.page.locator(self.activeCheckboxesSelector).all()

        return active_elements