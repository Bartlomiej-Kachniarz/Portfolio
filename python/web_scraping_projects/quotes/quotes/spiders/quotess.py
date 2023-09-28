import scrapy
from scrapy_splash import SplashRequest


class QuotessSpider(scrapy.Spider):
    name = "quotess"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    script = """
    """

    def parse(self, response):
        yield SplashRequest(url="https://quotes.toscrape.com/")
