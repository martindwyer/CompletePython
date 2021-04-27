from bs4 import BeautifulSoup

from course_contents.c12_browser_automation_selenium.lectures.l01_our_scraping_code.locators.quotes_page_locators import QuotesPageLocators
from course_contents.c12_browser_automation_selenium.lectures.l01_our_scraping_code.parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        return [QuoteParser(e) for e in self.soup.select(QuotesPageLocators.QUOTE)]
