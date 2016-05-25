import csv
import os, sys
year = '2013'
month = '07'
while not (int(year) == 2016 and int(month) == 02):
    if int(month) < 10:
        if len(str(month)) < 2:
            month = '0' + str(month)
    else:
        month = str(month)

    with open("/home/stephen/Documents/College/4th Year/4th Year Project/ReducedData/{}-{} - "
              "Citi Bike trip data.csv".format(year, month), "rb")\
            as fp_in, open("/home/stephen/Documents/College/4th Year/4th Year Project/ReducedData/newfile.csv", "wb")\
            as fp_out:
        w = csv.writer(fp_out)
        r = csv.reader(fp_in)
        for row in r:
            w.writerow(row)
    os.remove("/home/stephen/Documents/College/4th Year/4th Year Project/ReducedData/{}-{} - "
              "Citi Bike trip data.csv".format(year, month))
    with open("/home/stephen/Documents/College/4th Year/4th Year Project/ReducedData/newfile.csv", "rb") as fp_in, open\
            ("/home/stephen/Documents/College/4th Year/4th Year Project/ReducedData/{}-{} - "
             "Citi Bike trip data.csv".format(year, month), "wb")\
            as fp_out:
        w = csv.writer(fp_out)
        r = csv.reader(fp_in)
        i = 0
        for row in r:
            if i == 0:
                w.writerow(row)
            elif i % 5 == 0:
                w.writerow(row)
            i += 1

        if int(month) == 12:
            month = 1
            year = int(year) + 1
        else:
            month = int(month) + 1
    print '/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/{}-{} - ' \
          'Citi Bike trip data.csv'.format(year, month)