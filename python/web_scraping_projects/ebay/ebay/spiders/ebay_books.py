import scrapy


class EbayBooksSpider(scrapy.Spider):
    name = "ebay_books"
    allowed_domains = ["www.ebay.com"]
    # start_urls = ["https://www.ebay.com/b/Textbooks/1105/bn_226752"]

    def start_requests(self):
        yield scrapy.Request(url='https://www.ebay.com/b/Textbooks/1105/bn_226752',
                             callback=self.parse, headers={
                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
                             })

    def parse(self, response):
        for product in response.xpath("//section/ul/li[@class='s-item s-item--large']"):

            title = product.xpath(
                ".//div/div[2]/a/h3[@class='s-item__title']/text()").get()
            url = product.xpath(".//div/div[2]/a/@href").get()
            current_price = product.xpath(
                ".//div[@class='s-item__detail s-item__detail--primary']/span[@class='s-item__price']/text()").get()
            if not current_price:
                current_price = product.xpath(
                    ".//div[@class='s-item__detail s-item__detail--primary']/span[@class='s-item__price']/span[@class='ITALIC']/text()").get()
            original_price = product.xpath(
                ".//div[@class='s-item__detail s-item__detail--primary']/span[@class='s-item__trending-price']/span[@class='STRIKETHROUGH']/text()").get()
            shipping = product.xpath(
                ".//div/div/span[@class='s-item__shipping s-item__logisticsCost']/text()").get()
            product_options = product.xpath(
                ".//div[@class='s-item__detail s-item__detail--primary']/span[@class='s-item__purchase-options s-item__purchaseOptions']/text()").get()
            user_agent = response.request.headers['User-Agent']

            yield {
                'title': title,
                'url': url,
                'current_price': current_price,
                'original_price': original_price,
                'shipping': shipping,
                'product_options': product_options,
                'User-Agent': user_agent
            }

        next_page = response.xpath(
            "//a[@class='pagination__next icon-link']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
                                 })
