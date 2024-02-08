import pages
import pytest
class TestFooter:
    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        actual_result = pages.index_page.get_text_from_halyk_login_button(page)
        assert actual_result == 'Google-мен іздеу', 'Google Search button text is not correct'
