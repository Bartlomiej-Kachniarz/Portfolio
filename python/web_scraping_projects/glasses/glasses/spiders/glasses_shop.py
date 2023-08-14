import scrapy


class GlassesShopSpider(scrapy.Spider):
    name = "glasses_shop"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        for product in response.xpath(
            '//div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'
        ):
            product_url = {}
            product_image_link = {}
            product_name = {}
            product_price = {}
            colors_counter = 1

            for color in product.xpath('.//div[@class="product-img-outer"]'):
                product_url = color.xpath(f".//a[{colors_counter}]/@href").get()
                product_image_link = color.xpath(f".//a[{colors_counter}]/img/@data-src").get()
                colors_counter += 1

            colors_counter = 1
            for color in product.xpath('.//div[@class="row no-gutters"]'):
                product_name = color.xpath(f'.//div/div[@class="p-title"]/a[{colors_counter}]/@title').get()
                product_price = color.xpath(".//div/span/text()").get()
                colors_counter += 1

            yield {
                "product_url": product_url,
                "product_image_link": product_image_link,
                "product_name": product_name,
                "product_price": product_price,
            }

        next_page = response.xpath('//ul/li[6]/a[@class="page-link"]/@href').get()

        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                },
            )
