import pages
import pytest
class TestFooter:
    def home_page_is_available(self, page):
        pages.index_page.open_index_page(page)
        actual_result = pages.IndexPage.logo_is_available()
        assert actual_result == True, "Страница недоступна"
    # def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
    #     pages.index_page.open_index_page(page)
    #     actual_result = pages.index_page.get_text_from_halyk_login_button(page)
    #     assert actual_result == ' Войти ', 'Не найдено'

