import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Books2scrapeSpider(CrawlSpider):
    name = "books2scrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"  # noqa: E501

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ol/li/article/h3/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths="//section/div/div/ul/li/a")),
    )

    custom_settings = {"FEEDS": {f"books_to_scrape{name}.csv": {"format": "csv"}}}

    def parse_item(self, response):
        response_title = response.xpath("normalize-space(//div/h1/text())").get()
        response_price = response.xpath("normalize-space(//article/div[1]/div[2]/p[1]/text())").get()
        response_available = response.xpath("normalize-space(//article/div[1]/div[2]/p[2]/text()[2])").get()

        yield {
            "title": response_title,
            "price": response_price,
            "available": response_available,
            "url": response.url,
        }
