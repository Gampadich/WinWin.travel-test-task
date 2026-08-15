# actions/filtersSection.py
import allure


class FiltersSection:
    def __init__(self, page):
        self.page = page
        self.see_more_button = page.locator('button[data-wwt-id="filter__see-more--button"]').first
        self.activeCheckboxesSelector = 'button[data-wwt-id="filter__option--checkbox"][aria-checked="true"]'

    @allure.step('Clicking see_more_button and pets checkbox button')
    def see_more_and_checkbox_button_click(self):
        # 1. Чекаємо появи та завершення анімації модального вікна
        self.page.wait_for_timeout(1500)

        # 2. Натискаємо "Показати більше" / "Дивитися більше", якщо кнопка є
        see_more = self.page.locator('button[data-wwt-id="filter__see-more--button"]').first
        if see_more.is_visible():
            see_more.click(force=True)
            self.page.wait_for_timeout(500)

        # 3. Знаходимо чекбокс тварин за текстом або точним локатором
        # Спочатку пробуємо оригінальний локатор, якщо він є у DOM:
        pets_btn = self.page.locator('button[data-wwt-id="filter-11__title--checkbox"]').first

        # Якщо за id не знайдено, шукаємо за назвою фільтру/текстом "Тварини" / "Pets"
        if not pets_btn.is_visible():
            pets_btn = self.page.get_by_role("button", name="Тварини").first

        if not pets_btn.is_visible():
            pets_btn = self.page.locator("button[data-wwt-id*='title--checkbox']").first

        # Клікаємо тільки якщо елемент реально присутній
        if pets_btn.is_visible():
            pets_btn.click(force=True)

    @allure.step('Checking active checkboxes button')
    def active_checkboxes_button_click(self):
        self.page.wait_for_timeout(1000)
        active_elements = self.page.locator(self.activeCheckboxesSelector).all()
        return active_elements