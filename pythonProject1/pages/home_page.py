from playwright.sync_api import Page
import config


class HomePage:
    _BUTTON_HALYK_LOGIN = f'text=Войти'
    _BUTTON_SELECT_CITY = '[aria-label="Смена города, текущий город"]'
    _BUTTON_SELECT_LANGUAGE = '//div[@class="panel-item panel-item-dropdown" and contains(text(), "Русский")]'
    _BUTTON_HALYK_BANK = '//div[@class="panel-item" and contains(text(), "Halyk bank")]'
    _BUTTON_HOMEBANK = '//div[@class="panel-item" and contains(text(), "Homebank")]'
    _BUTTON_CALL_CENTER = '//div[@class="panel-item" and contains(text(), "77 111")]'

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(config.url.BASE_URL)

    def is_element_visible(self, selector):
        return self.page.locator(selector).is_visible()
    # def get_text_from_elements(self, page: Page, text) -> None:
    #     page.get_by_text(self, text)
    #
    # def get_text_from_halyk_login_button(self, page: Page) -> None:
    #     return page.locator(self._BUTTON_HALYK_LOGIN).get_attribute('value')
    #
    # def logo_is_available(self, page: Page):
    #     return page.get_by_alt_text(self._HALYK_LOGO).nth(0).is_visible()
    #
    # def get_text_from_halyk_search_bar(self, page: Page):
    #     return page.locator(self._HALYK_SEARCH_BAR).nth(0).is_visible()

# def select_city_from_cities_list(self, page: Page): -> None:
#     return
