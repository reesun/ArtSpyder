# -*- coding: utf-8 -*-

__author__ = 'yyy'

import psycopg2

def get_conn():
    conn = psycopg2.connect(dbname='wikiart', user='postgres', host='127.0.0.1')
    cur = conn.cursor()
    return conn, cur



if __name__ == "__main__":

    conn, cur = get_conn()
    cur.execute("SELECT * FROM users;")
    print cur.fetchone()

    cur.close()
    conn.close()
