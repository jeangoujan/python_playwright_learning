from playwright.sync_api import Page
import config


class HomePage:
    # Header
    _BUTTON_HALYK_LOGIN = f'text=Войти'
    _BUTTON_SELECT_CITY = '[aria-label="Смена города, текущий город"]'
    _BUTTON_SELECT_LANGUAGE = '//div[@class="panel-item panel-item-dropdown" and contains(text(), "Русский")]'
    _BUTTON_HALYK_BANK = '//div[@class="panel-item" and contains(text(), "Halyk bank")]'
    _BUTTON_HOMEBANK = '//div[@class="panel-item" and contains(text(), "Homebank")]'
    _BUTTON_CALL_CENTER = '//div[@class="panel-item" and contains(text(), "77 111")]'

    # Main Header
    _HALYK_MARKET_LOGO = '//img[@src="/_nuxt/30f70ea43b8383d02d9fade5c7f222d7.svg"]'
    _HALYK_SEARCH_BAR = 'input.search-input[placeholder="Найти в Halyk Market"]'
    _HALYK_FAVORITES = '//span[contains(@class, "icon-text") and contains(text(), "Избранное")]'
    _HALYK_CART = '//span[contains(@class, "icon-text") and contains(text(), "Корзина")]'

    # Category-bar --------------------------------------------------------------------------------
    _CATEGORY_BUTTON = 'button.btn.navbar-button.navbar-trigger.filled.small[aria-label="Просмотреть все категории"]'
    _PROMOTIONS_BUTTON = 'li.navbar-item > a[href="/promotion/all"]'
    _PHONES_GADGETS = 'li.navbar-item > a[href="/category/telefoni-i-gadzheti"]'
    _KITCHEN_EQUIPMENT_BUTTON = 'li.navbar-item > a[href="/category/kuhonnaya-tehnika"]'
    _SPORT_BUTTON = 'li.navbar-item > a[href="/category/dosug"]'
    _FURNITURE_BUTTON = 'li.navbar-item > a[href="/category/mebel"]'

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(config.url.BASE_URL)

    def is_element_visible(self, selector):
        return self.page.locator(selector).is_visible()
