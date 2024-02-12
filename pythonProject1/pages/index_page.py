from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_HALYK_LOGIN = "//div[contains(text(), ' Войти ')]"
    # //div[@class='FPdoLc lJ9FBc']//input[@name='btnK']

    _BUTTON_SELECT_CITY = ".topbar-side--left > .dropdown:nth-child(1) .panel-item"
    _HALYK_ICON = "css=.app-toolbar-logo img"
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)



    def get_text_from_halyk_login_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_HALYK_LOGIN).get_attribute('value')

    # def select_city_from_cities_list(self, page: Page): -> None:
    #     return
    def logo_is_available(self, page: Page):
        return page.locator(self._HALYK_ICON).is_visible()

