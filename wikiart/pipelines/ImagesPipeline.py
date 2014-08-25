# -*- coding: utf-8 -*-
__author__ = 'huangxiran'

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return 'portrait/artists/%s' % (image_guid)

    def get_media_requests(self, item, info):
        image_url = item['artist_avatar']
        yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item