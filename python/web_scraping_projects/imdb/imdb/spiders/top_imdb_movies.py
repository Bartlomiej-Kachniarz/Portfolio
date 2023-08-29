# pylint: disable=C0301
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TopImdbMoviesSpider(CrawlSpider):
    name = "top_imdb_movies"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]
    user_agent = """Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"""  # noqa: E501

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[@class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b85248f1-7 lhgKeb cli-title"]/a'  # noqa: E501
            ),
            callback="parse_item",
            follow=True,
        ),
    )

    def parse_item(self, response):
        yield {
            "title": response.xpath('//span[@class="sc-afe43def-1 fDTGTb"]/text()').get(),
            "year": response.xpath(
                '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[1]/a/text()'  # noqa: E501
            ).get(),
            "duration": response.xpath(
                '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[3]/text()'  # noqa: E501
            ).get(),
            "genre": response.xpath("//section/div[1]/div/a/span/text()").get(),
            "rating": response.xpath(
                '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div[1]/a/span/div/div[2]/div[1]/span[1]/text()'  # noqa: E501
            ).get(),
            "url": response.url,
        }
