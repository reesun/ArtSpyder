# -*- coding: utf-8 -*-
__author__ = 'huangxiran'

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

from wikiart.items import WikiartProductsItem
from wikiart.items import WikiartItem

class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        pre_path = request.url.split('/')[-2]
        image_guid = request.url.split('/')[-1]
        return 'images/%s/%s' % (pre_path, image_guid)

    def get_media_requests(self, item, info):
        if isinstance(item, WikiartProductsItem):
            image_url = item['resource_url']
        elif isinstance(item, WikiartItem):
            image_url = item['artist_avatar']
        yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item