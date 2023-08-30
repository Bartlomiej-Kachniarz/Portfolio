import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Rating10kSpider(CrawlSpider):
    name = "rating_10k"
    allowed_domains = ["www.imdb.com"]
    start_urls = [
        "https://www.imdb.com/search/title/?title_type=feature,tv_movie,documentary,short&num_votes=10000,&sort=user_rating,desc"  # noqa: E501
    ]
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"  # noqa: E501

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths="//div/h3/a"),
            callback="parse_item",
            follow=True,
        ),
        Rule(LinkExtractor(restrict_xpaths='//div[3]/div/div/div/a[@class="lister-page-next next-page"]')),
    )

    def parse_item(self, response):
        year_path = response.xpath("//section/section/div/section/section/div/div/ul/li[1]/a/text()").get()
        if year_path is None:
            year_path = response.xpath("//section/section/div/section/section/div/div/ul/li[2]/a/text()").get()

        yield {
            "title": response.xpath('//span[@class="sc-afe43def-1 fDTGTb"]/text()').get(),
            "year": year_path,
            "duration": response.xpath("//section/section/div/section/section/div/div/ul/li[last()]/text()").get(),
            "genre": response.xpath("//section/div[1]/div/a/span/text()").get(),
            "rating": response.xpath("//div/div/div/div/div/a/span/div/div/div/span[1]/text()").get(),
            "url": response.url,
        }
