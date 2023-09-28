import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = "coin"
    allowed_domains = ["web.archive.org"]
    start_urls = ["http://web.archive.org/web/20200116052415/https://www.livecoin.net/en/"]

    script = """
    function main(splash, args)
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(10))
        rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
        rur_tab[1]:mouse_click()
            assert(splash:wait(10))
        splash:set_viewport_full()
        return splash:html()
    end

    """

    def start_requests(self):
        yield SplashRequest(
            url="http://web.archive.org/web/20200116052415/https://www.livecoin.net/en/",
            callback=self.parse,
            endpoint="execute",
            args={"lua_source": self.script, "timeout": 90, "resource_timeout": 3000},
        )

    def parse(self, response):
        for currency in response.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS')]"):
            yield {
                "currency_pair": currency.xpath(".//div/div/text()").get(),
                "volume(24h)": currency.xpath(".//div[2]/span/text()").get(),
            }
