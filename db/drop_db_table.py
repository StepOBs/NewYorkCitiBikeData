import sqlite3 as lite
import csv
con = lite.connect('bike_data.db')
con.text_factory = str
with con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS bikes')
con.close()