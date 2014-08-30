# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WikiartItem(scrapy.Item):
    artist_url = scrapy.Field()
    artist_name = scrapy.Field()
    artist_avatar = scrapy.Field()
    born = scrapy.Field()
    died = scrapy.Field()
    nationality = scrapy.Field()

class WikiartProductsItem(scrapy.Item):

    product_name = scrapy.Field()
    create_at = scrapy.Field()
    resource_url = scrapy.Field()
    s_url = scrapy.Field()
    create_by = scrapy.Field()
    width = scrapy.Field()
    length = scrapy.Field()
    product_style = scrapy.Field()
    product_genre = scrapy.Field()
    dimensions = scrapy.Field()
    material = scrapy.Field()



