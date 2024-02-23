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

    def test_halyk_link(self, home_page, page):
        home_page.open_page()
        assert home_page.is_link_works(home_page._BUTTON_HALYK_BANK), "Переход по ссылке Halyk Bank не работает"
        assert home_page.page.url == config.url.HALYK_BANK_URL, f"Неверный URL после перехода. Ожидался {config.url.HALYK_BANK_URL}, получен {page.url}"

    def test_homebank_link(self, home_page, page):
        home_page.open_page()
        assert home_page.is_link_works(home_page._BUTTON_HOMEBANK), "Переход по ссылке Homebank не работает"
        assert home_page.page.url == config.url.HALYK_HOMEBANK_URL, f"Неверный URL после перехода. Ожидался {config.url.HALYK_HOMEBANK_URL}, получен {page.url}"

    def test_login_modal_is_available_to_use(self, home_page, page):
        home_page.open_page()
        assert home_page.auth_modal_click(), "Модальное окно авторизации недоступно"

    def test_favorites_link(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page._HALYK_FAVORITES), "Переход на страницу 'Избранное' не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.HALYK_FAVORITE_ENDPOINT, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.HALYK_FAVORITE_ENDPOINT}, получен {page.url}"

    # BANNERS-CHECK=====================================================================================================
    def test_first_banner(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page.BANNER_NEDELYA_VIGODI), "Баннер 'Неделя выгоды' не отображается"
        assert home_page.link_checking(home_page.BANNER_NEDELYA_VIGODI), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.NEDELYA_VIGODI, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.NEDELYA_VIGODI}, получен {page.url}"

    def test_second_banner(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(
            home_page.BANNER_IGROVIE_PRISTAVKI), "Баннер 'Игровые приставки' не отображается"
        assert home_page.link_checking(home_page.BANNER_IGROVIE_PRISTAVKI), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.IGROVIE_PRISTAVKI, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.IGROVIE_PRISTAVKI}, получен {page.url}"

    def test_third_banner(self, home_page, page):
        home_page.open_page()
        home_page.next_banner_slide(home_page.next_slide_button, 1)
        assert home_page.is_element_visible(
            home_page.BANNER_IGROVIE_PRISTAVKI2), "Баннер 'Игровые приставки' не отображается"
        assert home_page.link_checking(home_page.BANNER_IGROVIE_PRISTAVKI2), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.IGROVIE_PRISTAVKI, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.IGROVIE_PRISTAVKI}, получен {page.url}"

    def test_fourth_banner(self, home_page, page):
        home_page.open_page()
        home_page.next_banner_slide(home_page.next_slide_button, 2)
        assert home_page.is_element_visible(
            home_page.BANNER_JEWELLERY), "Баннер 'Неделя выгоды - 'Украшения' не отображается"
        assert home_page.link_checking(home_page.BANNER_JEWELLERY), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.JEWELLERY, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.JEWELLERY}, получен {page.url}"

    def test_fiveth_banner(self, home_page, page):
        home_page.open_page()
        home_page.next_banner_slide(home_page.next_slide_button, 3)
        assert home_page.is_element_visible(
            home_page.BANNER_PERFUME), "Баннер 'Неделя выгоды - 'Парфюмерия' не отображается"
        assert home_page.link_checking(home_page.BANNER_PERFUME), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.PERFUME, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.PERFUME}, получен {page.url}"

    def test_sixth_banner(self, home_page, page):
        home_page.open_page()
        home_page.next_banner_slide(home_page.next_slide_button, 4)
        assert home_page.is_element_visible(
            home_page.BANNER_TVS), "Баннер 'Неделя выгоды - 'Телевизоры' не отображается"
        assert home_page.link_checking(home_page.BANNER_TVS), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.TELEVIZORI, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.TELEVIZORI}, получен {page.url}"

    def test_seventh_banner(self, home_page, page):
        home_page.open_page()
        home_page.next_banner_slide(home_page.next_slide_button, 5)
        assert home_page.is_element_visible(
            home_page.BANNER_KITCHEN_SALE), "Баннер 'Неделя выгоды - 'Термомикс + подарок' не отображается"
        assert home_page.link_checking(home_page.BANNER_KITCHEN_SALE), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.KITCHEN_SALE, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.KITCHEN_SALE}, получен {page.url}"

    def test_eighth_banner(self, home_page, page):
        home_page.open_page()
        home_page.next_banner_slide(home_page.next_slide_button, 6)
        assert home_page.is_element_visible(
            home_page.BANNER_SMARTPHONES), "Баннер 'Неделя выгоды - 'Смартфоны' не отображается"
        assert home_page.link_checking(home_page.BANNER_SMARTPHONES), "Переход на баннер не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.SMARTPHONES, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.SMARTPHONES}, получен {page.url}"

    # ===================================================================================================================

    # CATEGORIES-CHECK==================================================================================================

    def test_telefony_i_gadzheti(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_PHONES_AND_GADGETS), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.PHONES_AND_GADGETS, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.PHONES_AND_GADGETS}, получен {page.url}"

    # todo China Goods

    def test_health_and_beauty(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_BEAUTY_AND_HEALTH), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.HEALTH_AND_BEAUTY, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.HEALTH_AND_BEAUTY}, получен {page.url}"

    def test_laptops_and_pc(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_LAPTOPS_AND_PC), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.LAPTOS_AND_PC, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.LAPTOS_AND_PC}, получен {page.url}"

    def test_kitchen_equipment(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_KITCHEN_EQUIPMENT), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.KITCHEN_EQUIPMENT, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.KITCHEN_EQUIPMENT}, получен {page.url}"

    def test_home_appliances(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_HOME_APPLIANCES), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.HOME_APPLIANCES, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.HOME_APPLIANCES}, получен {page.url}"

    def test_televizors(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_TELEVISORS), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.TELEVIZORS, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.TELEVIZORS}, получен {page.url}"

    def test_construction_and_repair(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_CONSTRUCTION_AND_REPAIR), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.CONSTRUCTION_AND_REPAIR, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.CONSTRUCTION_AND_REPAIR}, получен {page.url}"

    def test_photo_and_video(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_PHOTO_AND_VIDEO), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.PHOTO_AND_VIDEO, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.PHOTO_AND_VIDEO}, получен {page.url}"

    def test_autogoods(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_AUTOGOODS), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.AUTOGOODS, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.AUTOGOODS}, получен {page.url}"

    def test_furniture(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_FURNITURE), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.FURNITURE, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.FURNITURE}, получен {page.url}"

    def test_sport_and_rest(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_SPORT_AND_REST), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.SPORT_AND_REST, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.SPORT_AND_REST}, получен {page.url}"

    def test_jewelleries(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_JEWELLERY), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.JEWELLERY_ACCESORIES, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.JEWELLERY_ACCESORIES}, получен {page.url}"

    def test_pharmacy(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_PHARMACY), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.PHARMACY, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.PHARMACY}, получен {page.url}"

    def test_clothes(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_CLOTHES), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.CLOTHES, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.CLOTHES}, получен {page.url}"

    def test_shoes(self, home_page, page):
        home_page.open_page()
        assert home_page.link_checking(home_page.CATEGORIES_SHOES), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.SHOES, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.SHOES}, получен {page.url}"

    @pytest.mark.categories
    def test_accesories(self, home_page, page):
        home_page.open_page()
        home_page.next_banner_slide(home_page.categories_next_slide_button, 6)
        assert home_page.link_checking(home_page.CATEGORIES_BEAUTY_AND_HEALTH), "Переход на категорию не работает"
        assert home_page.page.url == config.url.BASE_URL + config.url.HEALTH_AND_BEAUTY, f"Неверный URL после перехода. Ожидался {config.url.BASE_URL + config.url.HEALTH_AND_BEAUTY}, получен {page.url}"

    # def test_promotions_link(self, home_page, page):
    #     home_page.open_page()
    #     assert home_page.is_link_works(home_page._PROMOTIONS_BUTTON), "Переход на страницу 'Акции' не работает"
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
