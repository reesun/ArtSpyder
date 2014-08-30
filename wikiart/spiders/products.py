# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from wikiart.items import WikiartProductsItem

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["wikiart.org"]

    # 留一个接口，去Artists表中取艺术家
    start_urls = (
        'http://www.wikiart.org/en/ivan-aivazovsky',
    )

    def parse(self, response):

        _link = "http://www.wikiart.org"

        hxs = HtmlXPathSelector(response)
        for sel in hxs.select("//div[@class='pb5']"):
            linkArray = sel.xpath('a/@href').extract()
            link = _link + linkArray[0]
            yield Request(url=link, callback=self.parse_product)


    def parse_product(self, response):
        product = WikiartProductsItem()

        hxs = HtmlXPathSelector(response)

        product['s_url'] = response._url
        product['product_name'] = hxs.xpath("//div[@class='tt30 pb8']/h1/text()").extract()[0]

        product_info = hxs.xpath("//div[@class='ArtistInfo']")

        image_info = product_info.xpath("//a[@id='paintingImage']/@href").extract()[0]
        product['resource_url'] = image_info

        for data_info in product_info.xpath("//div[@class='DataProfileBox']/p"):
            key = data_info.xpath("b/text()").extract()[0]
            if key == 'Material:':
                value = data_info.xpath("text()").extract()[1]
                value = value.replace("\r\n", '')
                product['material'] = value
            elif key == 'Dimensions:':
                value = data_info.xpath("text()").extract()[1]
                value = value.replace("\r\n", '')
                product['dimensions'] = value

        product['create_by'] = hxs.xpath("//a[@itemprop='author']/text()").extract()[0]
        years = product_info.xpath("//span[@itemprop='dateCreated']/text()").extract()
        if len(years) > 0:
            product['create_at'] = years[0]
        else:
            product['create_at'] = 'UnKnown'

        product['product_style'] = product_info.xpath("//span[@itemprop='style']/text()").extract()
        product['product_genre'] = product_info.xpath("//span[@itemprop='genre']/text()").extract()

        return product

        #p_size_lis = p_size_sel.xpath("li")


