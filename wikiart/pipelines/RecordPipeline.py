# -*- coding: utf-8 -*-
__author__ = 'yyy'

from wikiart.utils import DBUtils
from wikiart.items import WikiartProductsItem
from wikiart.items import WikiartItem

class RecordPipeline(object):
    def __init__(self):
        self.conn, self.cur = DBUtils.get_conn()

    def process_item(self, item, spider):
        if isinstance(item, WikiartProductsItem):
            sql = """INSERT INTO products_details(resource_url, resource_type, create_by, product_name, s_url,
                    post_type, dimensions, create_at, material)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cur.execute(sql, (item['resource_url'], '1', item['create_by'], item['product_name'],
                                item['s_url'], '2', item['dimensions'], item['create_at'], item['material']))
        elif isinstance(item, WikiartItem):
            sql = """INSERT INTO artists(artist_url, artist_name, born, nationality, is_down, artist_avatar, died)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            self.cur.execute(sql, (item['artist_url'], item['artist_name'], item['born'],
                    item['nationality'], 'false', item['artist_avatar'], item['died']))

        self.conn.commit()

        return item

    def __del__(self):
        self.cur.close()
        self.conn.close()