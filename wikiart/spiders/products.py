# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["wikiart.org"]
    start_urls = (
        'http://www.wikiart.org/en/julius-evola',
    )

    def parse(self, response):
        pass
