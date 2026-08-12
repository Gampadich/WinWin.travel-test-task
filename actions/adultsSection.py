import allure

class AdultsSection:
    def __init__(self, page):
        self.page = page
        self.guests_select_button = page.locator('button[data-wwt-id="guests-select__open--button"]').first
        self.counter_button = page.locator('button[data-wwt-id="number-counter__plus--button"]').first
        self.counter = page.locator('input[data-wwt-id="number-counter__input--input"]').first

    @allure.step('Clicking quests select button')
    def quests_select_button_click(self):
        return self.guests_select_button.click()

    @allure.step('Clicking plus adult button while it available')
    def plus_button_clicking(self):
        while True:
            if self.counter_button.is_disabled():
                break
            else:
                self.counter_button.click()
        return self.counter
