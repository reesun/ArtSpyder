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


