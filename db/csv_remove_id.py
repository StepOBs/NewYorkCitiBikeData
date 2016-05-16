import csv
import os, sys
with open("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/2014-09 - Citi Bike trip data.csv", "rb")\
        as fp_in, open("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/newfile.csv", "wb")\
        as fp_out:
    w = csv.writer(fp_out)
    r = csv.reader(fp_in)
    for row in r:
        del row[3]
        del row[6]
        w.writerow(row)
os.remove("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/2014-09 - Citi Bike trip data.csv")
with open("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/newfile.csv", "rb") as fp_in, open\
        ("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/2014-09 - Citi Bike trip data.csv", "wb")\
        as fp_out:
    w = csv.writer(fp_out)
    r = csv.reader(fp_in)
    for row in r:
        w.writerow(row)
