import sqlite3 as lite
import csv
con = lite.connect('bike_data.db')
con.text_factory = str
year = 2013
month = 7
with con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS bikes')
    cur.execute("CREATE TABLE bikes(tripduration, starttime, stoptime, start_station_name,"
                "start_station_latitude, start_station_longitude, end_station_name,"
                "end_station_latitude, end_station_longitude, bikeid, usertype, birth_year, gender);")
    while not (year == 2016 and month == 1):
        print 'entered while'
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        db_file = '/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/{}-{} - Citi' \
                  ' Bike trip data.csv'.format(str(year), str(month))
        with open(db_file, 'rb') as fin:
            print 'reading {}'.format(db_file)
            dr = csv.DictReader(fin)
            to_db = [(i['tripduration'], i['starttime'], i['stoptime'], i['start station name'],
                      i['start station latitude'], i['start station longitude'], i['end station name'],
                      i['end station latitude'], i['end station longitude'], i['bikeid'], i['usertype'], i['birth year'],
                      i['gender']) for i in dr]
            cur.executemany('INSERT INTO bikes(tripduration, starttime, stoptime,'
                            'start_station_name, start_station_latitude, start_station_longitude,'
                            'end_station_name, end_station_latitude, end_station_longitude, bikeid, usertype,'
                            'birth_year, gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', to_db)
        print month
        if (str(month)[0]) == '0':
            month = str(month)[1]
            month = int(month)
        print month
        print type(month)
        month = int(month)
        if month < 12:
            print 'if'
            month += 1
            year = year
        else:
            print 'else'
            month = 1
            year += 1
        print month
        print type(month)
con.close()