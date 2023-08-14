import scrapy


class GDPDebtSpider(scrapy.Spider):
    name = "gdp_debt"
    allowed_domains = ["www.worldpopulationreview.com"]
    start_urls = ["https://www.worldpopulationreview.com/country-rankings/countries-by-national-debt"]

    def parse(self, response):
        countries = response.xpath(
            '//*[@id="__next"]/div/div[3]/section[1]/div[1]/div[1]/div[3]/div[1]/table/tbody/tr[position() > 1]'
        )
        for country in countries:
            name = country.xpath(".//td[position() = 2]//text()").get()
            debt = country.xpath(".//td[position() = 3]//text()").get()

            yield {"name": name, "debt": debt}
