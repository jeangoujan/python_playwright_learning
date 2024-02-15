import pytest
import pages
from pages.home_page import HomePage


class TestHomePage:
    @pytest.fixture()
    def home_page(self, page):
        return HomePage(page)

    def test_login_button_is_available(self, home_page, page):
        home_page.open_page()
        assert home_page.is_element_visible(home_page._BUTTON_HALYK_LOGIN), "Кнопка 'Войти' не отображается на странице."
    # def test_home_page_is_available(self, page):
    #     pass
    #     # pages.home_page.open_page(page)
    #     # actual_result = pages.home_page.logo_is_available(page)
    #
    # def test_search_is_available(self, page):
    #     pass
    #     # pages.home_page.open_page(page)
    #     # assert pages.home_page.get_text_from_halyk_search_bar(page) == True, "Поиск на главной странице недоступен"
    #

    # def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
    #     pages.index_page.open_index_page(page)
    #     actual_result = pages.index_page.get_text_from_halyk_login_button(page)
    #     assert actual_result == ' Войти ', 'Не найдено'
