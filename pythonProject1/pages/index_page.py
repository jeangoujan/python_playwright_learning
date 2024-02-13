from playwright.sync_api import Page
import config
import pages



class IndexPage:
    _BUTTON_HALYK_LOGIN = "Войти"

    _BUTTON_SELECT_CITY = ".topbar-side--left > .dropdown:nth-child(1) .panel-item"
    _HALYK_LOGO = "логотип Halyk Market"
    _HALYK_SEARCH_BAR = "//*[@placeholder='Найти в Halyk Market']"



    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.BASE_URL)


    
    
    def get_text_from_elements(self, page: Page) -> None:
        page.get_by_text(self, page)

    def get_text_from_halyk_login_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_HALYK_LOGIN).get_attribute('value')


    def logo_is_available(self, page: Page):
        return page.get_by_alt_text(self._HALYK_LOGO).nth(0).is_visible()

    def get_text_from_halyk_search_bar(self, page: Page):
        return page.locator(self._HALYK_SEARCH_BAR).nth(0).is_visible()




# def select_city_from_cities_list(self, page: Page): -> None:
    #     return

