# -*- coding: utf-8 -*-

# Scrapy settings for wikiart project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wikiart'

SPIDER_MODULES = ['wikiart.spiders']
NEWSPIDER_MODULE = 'wikiart.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wikiart (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    'wikiart.pipelines.ImagesPipeline.MyImagesPipeline',
    'wikiart.pipelines.RecordPipeline.RecordPipeline',
    ]

IMAGES_STORE = '/Users/yyy/myCode/yuntoo/download'