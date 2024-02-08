import config
from playwright.sync_api import Page

class IndexPage:
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)
