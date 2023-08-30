# pylint: disable=C0301
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TopImdbMoviesSpider(CrawlSpider):
    name = "top_imdb_movies"
    allowed_domains = ["imdb.com"]
    user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        + " (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.imdb.com/chart/top/?ref_=nv_mv_250", headers={"User-Agent": self.user_agent}
        )

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths="//section/div/div[2]/div/ul/li/div[2]/div/div/div[1]/a"),  # noqa: E501
            callback="parse_item",
            follow=True,
            process_request="set_user_agent",
        ),
    )

    def set_user_agent(self, request, spider):
        request.headers["User-Agent"] = self.user_agent
        return request

    def parse_item(self, response):
        year_path = response.xpath(
            "//section/section/div/section/section/div/div/ul/li[1]/a/text()"  # noqa: E501
        ).get()
        if year_path is None:
            year_path = response.xpath(
                "//section/section/div/section/section/div/div/ul/li[2]/a/text()"  # noqa: E501
            ).get()

        yield {
            "title": response.xpath('//span[@class="sc-afe43def-1 fDTGTb"]/text()').get(),
            "year": year_path,
            "duration": response.xpath(
                "//section/section/div/section/section/div/div/ul/li[last()]/text()"  # noqa: E501
            ).get(),
            "genre": response.xpath("//section/div[1]/div/a/span/text()").get(),
            "rating": response.xpath("//div/div/div/div/div/a/span/div/div/div/span[1]/text()").get(),  # noqa: E501
            "url": response.url,
            # "user-agent": response.request.headers['User-Agent']
        }
