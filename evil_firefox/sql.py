#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


con = lite.connect('/home/saurabh/.mozilla/firefox/pp0qyr8g.default/cookies.sqlite')

with con:

    cur = con.cursor()
    #cur.execute(".mode columns")
    #cur.execute(".headers on")
    cur.execute("SELECT * FROM moz_cookies")

    rows = cur.fetchall()

    for row in rows:
        print row
