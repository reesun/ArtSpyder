# -*- coding: utf-8 -*-
__author__ = 'yyy'

from wikiart.utils import DBUtils

class RecordPipeline(object):
    def __init__(self):
        self.conn, self.cur = DBUtils.get_conn()


    def process_item(self, item, spider):
        sql = """INSERT INTO artists(artist_url, artist_name, born, nationality, is_down, artist_avatar, died)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        self.cur.execute(sql, (item['artist_url'], item['artist_name'], item['born'],
                               item['nationality'], 'false', item['artist_avatar'], item['died']))
        self.conn.commit()

        return item

    def __del__(self):
        self.cur.close()
        self.conn.close()