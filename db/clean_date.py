import csv
from shutil import move
from tempfile import NamedTemporaryFile
with open('/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/2016-01 - Citi Bike trip data.csv', 'rb')\
        as csvfile, NamedTemporaryFile(dir=".", delete=False) as temp:
    w = csv.writer(temp)
    r = csv.reader(csvfile)
    headers = next(r, None)
    w.writerow(headers)
    for row in r:
        dt = row[1].split('/')
        dz = dt[2].split(' ')
        if int(dt[0]) < 10:
            dt[0] = '0' + dt[0]
        if int(dt[1]) < 10:
            dt[1] = '0' + dt[1]
        row[1] = dz[0] + '-' + dt[0] + '-' + dt[1] + ' ' + dz[1]

        ds = row[2].split('/')
        dy = ds[2].split(' ')
        if int(ds[0]) < 10:
            ds[0] = '0' + ds[0]
        if int(ds[1]) < 10:
            ds[1] = '0' + ds[1]
        row[2] = dy[0] + '-' + ds[0] + '-' + ds[1] + ' ' + dy[1]

        w.writerow(row)

move(temp.name, '/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/2016-01 - Citi Bike trip data.csv')