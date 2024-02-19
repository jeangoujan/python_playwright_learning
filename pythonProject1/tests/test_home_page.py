import pytest

import config
from pages.home_page import HomePage


class TestHomePage:
    # HEADER_ELEMENTS_AVAILABILITY: Logo, City, Language, HalykBank, Homebank, 77-111, Login ---------------------------
    @pytest.fixture()
    def home_page(self, page):
        return HomePage(page)

    def test_logo_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._HALYK_MARKET_LOGO), "Логотип недоступен"

    def test_city_selector_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._BUTTON_SELECT_CITY), "Кнопка выбора города недоступна"

    def test_language_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._BUTTON_SELECT_LANGUAGE), "Кнопка выбора языка недоступна"

    def test_halyk_bank_button_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._BUTTON_HALYK_BANK), "Кнопка 'Halyk Bank' недоступна"

    def test_homebank_button_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._BUTTON_HOMEBANK), "Кнопка 'Homebank' недоступна"

    def test_call_center_button_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._BUTTON_CALL_CENTER), "Кнопка '77-111' недоступна"

    def test_login_button_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._BUTTON_HALYK_LOGIN), "Кнопка 'Войти' недоступна"

    # Header: Logo, Search-bar, Favorites, Cart ---------------------------------------------------------

    def test_halyk_link(self, home_page, page):
        home_page.open_page()
        assert home_page.is_link_works(home_page._BUTTON_HALYK_BANK), "Переход по ссылке Halyk Bank не работает"
        assert home_page.page.url == config.url.HALYK_BANK_URL, f"Неверный URL после перехода. Ожидался {config.url.HALYK_BANK_URL}, получен {page.url}"

    def test_homebank_link(self, home_page, page):
        home_page.open_page()
        assert home_page.is_link_works(home_page._BUTTON_HOMEBANK), "Переход по ссылке Homebank не работает"
        assert home_page.page.url == config.url.HALYK_HOMEBANK_URL, f"Неверный URL после перехода. Ожидался {config.url.HALYK_HOMEBANK_URL}, получен {page.url}"

    @pytest.mark.login1
    def test_login_modal_is_available_to_use(self, home_page, page):
        home_page.open_page()
        assert home_page.click_login_button(), "Модальное окно авторизации недоступно"
    # def test_search_bar_is_available(self, home_page, page):
    #     home_page.open_page()
    #     search_bar = home_page.page.locator(home_page._HALYK_SEARCH_BAR)
    #     assert search_bar.first.is_visible(), "Поиск недоступен"
    #
    # def test_favorites_is_available(self, home_page, page):
    #     home_page.open_page()
    #     favorites = home_page.page.locator(home_page._HALYK_FAVORITES)
    #     assert favorites.first.is_visible(), "Избранные товары недоступны"
    #
    # def test_cart_is_available(self, home_page, page):
    #     home_page.open_page()
    #     cart = home_page.page.locator(home_page._HALYK_CART)
    #     assert cart.first.is_visible(), "Корзина недоступна"
    #
    # # Category-bar: Category, Promotions, Phones and Gadgets, Kitchen Equip, Sport, Furniture
    # @pytest.mark.first
    # def test_category_button_is_available(self, home_page, page):
    #     home_page.open_page()
    #     assert home_page.is_element_visible(home_page._CATEGORY_BUTTON), "Кнопка Категории недоступна"
    #
    # @pytest.mark.first
    # def test_promotions_button_is_available(self, home_page, page):
    #     home_page.open_page()
    #     assert home_page.is_element_visible(home_page._PROMOTIONS_BUTTON), "Кнопка 'Акции Halyk Market' недоступна"
    #
    # # @pytest.mark.first
    # def test_phones_button_is_available(self, home_page, page):
    #     home_page.open_page()
    #     assert home_page.is_element_visible(home_page._PHONES_GADGETS), "Кнопка 'Телефоны и гаджеты' недоступна"
    #
    # def test_kitchen_equip_button_is_available(self, home_page, page):
    #     home_page.open_page()
    #     assert home_page.is_element_visible(home_page._KITCHEN_EQUIPMENT_BUTTON), "Кнопка 'Кухонная техника' недоступна"
    #
    # def test_sport_button_is_available(self, home_page,page):
    #     home_page.open_page()
    #     assert home_page.is_element_visible(home_page._SPORT_BUTTON), "Кнопка 'Спорт и отдых' недоступна"
    #
    # def test_furniture_button_is_available(self, home_page, page):
    #     home_page.open_page()
    #     assert home_page.is_element_visible(home_page._FURNITURE_BUTTON), "Кнопка 'Мебель' недоступна"
