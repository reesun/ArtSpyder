# -*- coding: utf-8 -*-

__author__ = 'yyy'

import psycopg2

def get_conn():
    conn = psycopg2.connect(dbname='', user='postgres', password='', host='')
    cur = conn.cursor()
    return conn, cur



if __name__ == "__main__":

    conn, cur = get_conn()
    cur.execute("SELECT * FROM users;")
    print cur.fetchone()

    cur.close()
    conn.close()
