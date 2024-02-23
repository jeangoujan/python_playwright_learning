from playwright.sync_api import Locator, Page
import config


class HomePage:
    # Header
    _BUTTON_HALYK_LOGIN = f'text=Войти'
    _LOGIN_MODAL = '//div[@class="auth-modal-container"]'
    _BUTTON_SELECT_CITY = '[aria-label="Смена города, текущий город"]'
    _BUTTON_SELECT_LANGUAGE = '//div[@class="panel-item panel-item-dropdown" and contains(text(), "Русский")]'
    _BUTTON_HALYK_BANK = '//div[@class="panel-item" and contains(text(), "Halyk bank")]'
    _BUTTON_HOMEBANK = '//div[@class="panel-item" and contains(text(), "Homebank")]'
    _BUTTON_CALL_CENTER = '//div[@class="panel-item" and contains(text(), "77 111")]'

    # Banners===========================================================================================================
    BANNER_NEDELYA_VIGODI = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_09143_208178209139208179208190208180_3c9d5160b5.webp']"
    BANNER_IGROVIE_PRISTAVKI = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_Pristavki_dedf552a41.webp']"
    BANNER_IGROVIE_PRISTAVKI2 = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_Pristavki_FC_24_abc01ff635.webp']"
    BANNER_JEWELLERY = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_Yuvelirka_f281606dc1.webp']"
    BANNER_PERFUME = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_Parfyumeriya_97e31660f1.webp']"
    BANNER_TVS = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_Televizory_ab44955b53.webp']"
    BANNER_KITCHEN_SALE = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_market_tovary_banner_therm_59f52f5d93.webp']"
    BANNER_SMARTPHONES = "div.slide-image > img[src='https://cdn.halykmarket.kz/cms/uploads/medium_Smartfony_dbbd4ee492.webp']"

    next_slide_button = "section.slider.container div.swiper-button-next"

    def next_banner_slide(self, locator, clicks):
        for _ in range(clicks):
            self.page.locator(locator).click()
        self.page.wait_for_timeout(timeout=1000)
    # ==================================================================================================================

    # Categories========================================================================================================
    CATEGORIES_PHONES_AND_GADGETS = 'a.category.navigation-slide.swiper-slide.navigation-slide--active[href="/category/telefoni-i-gadzheti"]'
    #todo Товары из Китая
    CATEGORIES_BEAUTY_AND_HEALTH = 'a.category.navigation-slide.swiper-slide[href="/category/krasota-i-zdorove"]'
    CATEGORIES_LAPTOPS_AND_PC = 'a.category.navigation-slide.swiper-slide[href="/category/noutbuki-i-kompyuteri"]'
    CATEGORIES_KITCHEN_EQUIPMENT = 'a.category.navigation-slide.swiper-slide[href="/category/kuhonnaya-tehnika"]'
    CATEGORIES_HOME_APPLIANCES = 'a.category.navigation-slide.swiper-slide[href="/category/tehnika-dlya-doma"]'
    CATEGORIES_TELEVISORS = 'a.category.navigation-slide.swiper-slide[href="/category/televizori"]'
    CATEGORIES_CONSTRUCTION_AND_REPAIR = 'a.category.navigation-slide.swiper-slide[href="/category/stroitelstvo-i-remont-"]'
    CATEGORIES_PHOTO_AND_VIDEO = 'a.category.navigation-slide.swiper-slide[href="/category/foto-i-video"]'
    CATEGORIES_AUTOGOODS = 'a.category.navigation-slide.swiper-slide[href="/category/avtotovari"]'
    CATEGORIES_FURNITURE = 'a.category.navigation-slide.swiper-slide[href="/category/mebel"]'
    CATEGORIES_SPORT_AND_REST = 'a.category.navigation-slide.swiper-slide[href="/category/dosug"]'
    CATEGORIES_JEWELLERY = 'a.category.navigation-slide.swiper-slide[href="/category/ukrashenija-aksessuary"]'
    CATEGORIES_PHARMACY = 'a.category.navigation-slide.swiper-slide[href="/category/apteka"]'
    CATEGORIES_CLOTHES = 'a.category.navigation-slide.swiper-slide[href="/category/odezhda"]'
    CATEGORIES_SHOES = 'a.category.navigation-slide.swiper-slide[href="/category/obuv"]'
    #todo slide aksessuari
    CATEGORIES_ACCESORIES = 'a.category.navigation-slide.swiper-slide[href="/category/naruchnye-chasy-sumki-i-aksessuary"]'
    CATEGORIES_OFFICE_PRODUCTS = 'a.category.navigation-slide.swiper-slide[href="/category/kanceljarskie-tovary"]'
    CATEGORIES_DOSUG_ART = 'a.category.navigation-slide.swiper-slide[href="/category/dosug-i-tvorchestvo"]'
    CATEGORIES_HALYK_SHOP = 'a.category.navigation-slide.swiper-slide[href="/category/halyk-shop"]'
    CATEGORIES_GOODS_FOR_KIDS = 'a.category.navigation-slide.swiper-slide[href="/category/detskie-tovari"]'
    CATEGORIES_FLOWERS = 'a.category.navigation-slide.swiper-slide[href="/category/cvety"]'
    CATEGORIES_VITAMINS = 'a.category.navigation-slide.swiper-slide[href="/category/vitaminy-i-bad?f=loanPeriod%3A24"]'
    CATEGORIES_GOODS_FOR_HOME = 'a.category.navigation-slide.swiper-slide[href="/category/tovari-dlya-doma"]'
    CATEGORIES_GOODS_FOR_ANIMALS = 'a.category.navigation-slide.swiper-slide[href="/category/tovari-dlya-zhivotnih"]'

    categories_next_slide_button = 'div.category-list-swiper div.swiper-button-next'










    # Main Header
    _HALYK_MARKET_LOGO = '//img[@src="/_nuxt/30f70ea43b8383d02d9fade5c7f222d7.svg"]'
    _HALYK_SEARCH_BAR = 'input.search-input[placeholder="Найти в Halyk Market"]'
    _HALYK_FAVORITES = "//div[@class='toolbar-buttons app-toolbar-buttons']//div[@class='icon-wrap'][1]//span[@class='icon-text' and contains(text(), 'Избранное')]"
    _HALYK_CART = '//span[contains(@class, "icon-text") and contains(text(), "Корзина")]'

    # Category-bar --------------------------------------------------------------------------------
    _CATEGORY_BUTTON = 'button.btn.navbar-button.navbar-trigger.filled.small[aria-label="Просмотреть все категории"]'
    _PROMOTIONS_BUTTON = 'li.navbar-item > a[href="/promotion/all"]'
    _PHONES_GADGETS = 'li.navbar-item > a[href="/category/telefoni-i-gadzheti"]'
    _KITCHEN_EQUIPMENT_BUTTON = 'li.navbar-item > a[href="/category/kuhonnaya-tehnika"]'
    _SPORT_BUTTON = 'li.navbar-item > a[href="/category/dosug"]'
    _FURNITURE_BUTTON = 'li.navbar-item > a[href="/category/mebel"]'

    # Categories: ---------------------------------------------------------------------------------
    _PHONES_AND_GADGETS = ('a.category.navigation-slide.navigation-slide--active.swiper-slide.navigation-slide--active'
                           '.swiper-slide-active')
    _LAPTOPS_AND_PC = 'a.category.navigation-slide.swiper-slide.navigation-slide--active.swiper-slide-active'

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(config.url.BASE_URL)

    def is_element_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_link_works(self, locator):
        current_url_before_click = self.page.url
        popup_opened = [False]

        def on_popup(popup):
            self.page = popup
            popup_opened[0] = True

        self.page.once('popup', on_popup)
        self.page.locator(locator).click()
        self.page.wait_for_event('popup')
        if not popup_opened[0]:
            self.page.wait_for_load_state()
        current_url_after_click = self.page.url
        return current_url_before_click != current_url_after_click

    def auth_modal_click(self):
        self.page.locator(self._BUTTON_HALYK_LOGIN).click()
        return self.page.locator(self._LOGIN_MODAL).is_visible()

    def link_checking(self, locator):
        current_url_before_click = self.page.url
        self.page.locator(locator).click()
        self.page.wait_for_load_state()
        current_url_after_click = self.page.url

        return current_url_before_click != current_url_after_click


