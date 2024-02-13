import pages
import pytest
class TestHomePage:
    def test_home_page_is_available(self, page):
        pages.index_page.open_index_page(page)
        actual_result = pages.index_page.logo_is_available(page)
        assert actual_result == True, "Главная страница недоступна"

    def test_search_is_available(self, page):
        pages.index_page.open_index_page(page)
        assert pages.index_page.get_text_from_halyk_search_bar(page) == True, "Поиск на главной странице недоступен"




    # def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
    #     pages.index_page.open_index_page(page)
    #     actual_result = pages.index_page.get_text_from_halyk_login_button(page)
    #     assert actual_result == ' Войти ', 'Не найдено'

