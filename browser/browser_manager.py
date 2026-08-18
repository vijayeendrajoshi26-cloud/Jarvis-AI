from browser.search import SearchEngine
from browser.scraper import WebScraper
from browser.downloader import Downloader


class BrowserManager:

    def __init__(self):

        self.search_engine = SearchEngine()
        self.scraper = WebScraper()
        self.downloader = Downloader()

    def search(self, query):

        return self.search_engine.search(query)

    def scrape(self, url):

        return self.scraper.scrape(url)

    def download(self, url, filename=None):

        return self.downloader.download(
            url,
            filename
        )
    