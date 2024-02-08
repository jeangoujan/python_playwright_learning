from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_HALYK_LOGIN = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)



    def get_text_from_halyk_login_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_HALYK_LOGIN).get_attribute('value')



