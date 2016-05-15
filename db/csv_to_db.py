import sqlite3 as lite
import csv
con = lite.connect('bike_data.db')
con.text_factory = str
db_file = '/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/2016-01 - Citi Bike trip data.csv'
with con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS bikes_2016_01')
    cur.execute("CREATE TABLE bikes_2016_01(tripduration, starttime, stoptime, start_station_id, start_station_name,"
                "start_station_latitude, start_station_longitude, end_station_id, end_station_name,"
                "end_station_latitude, end_station_longitude, bikeid, usertype, birth_year, gender);")
    with open(db_file, 'rb') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['tripduration'], i['starttime'], i['stoptime'], i['start station id'], i['start station name'],
                  i['start station latitude'], i['start station longitude'], i['end station id'], i['end station name'],
                  i['end station latitude'], i['end station longitude'], i['bikeid'], i['usertype'], i['birth year'],
                  i['gender']) for i in dr]
        cur.executemany('INSERT INTO bikes_2016_01(tripduration, starttime, stoptime, start_station_id,'
                        'start_station_name, start_station_latitude, start_station_longitude, end_station_id,'
                        'end_station_name, end_station_latitude, end_station_longitude, bikeid, usertype, birth_year,'
                        'gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', to_db)