import requests

from course_contents.c12_browser_automation_selenium.lectures.l01_our_scraping_code.pages.quotes_page import QuotesPage

page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)
