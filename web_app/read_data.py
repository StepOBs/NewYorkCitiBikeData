import pandas as pd
#not currently in use
def read_data(start_date_month, start_date_year, end_date_month, end_date_year):
    if (start_date_month == end_date_month) and (start_date_year == end_date_year):
        df = pd.read_csv("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + start_date_year +
                         "-" + start_date_month + " - Citi Bike trip data.csv", sep=",")
    else:
        df = pd.read_csv("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + start_date_year +
                         "-" + start_date_month + " - Citi Bike trip data.csv", sep=",")
        while (int(start_date_year) != int(end_date_year)) and (int(start_date_month) != int(end_date_month)):
            print 'entered while'
            start_date_year = int(start_date_year)
            start_date_month = int(start_date_month)
            if start_date_month == 12:
                start_date_month = 1
                start_date_year += 1
            else:
                start_date_month += 1

            if start_date_month < 10:
                start_date_month = '0' + str(start_date_month)
            else:
                start_date_month = str(start_date_month)
            if end_date_month < 10:
                end_date_month = '0' + str(end_date_month)
            else:
                end_date_month = str(end_date_month)

            df1 = pd.read_csv("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" +
                              str(start_date_year) + "-" + start_date_month + " - Citi Bike trip data.csv", sep=",")
            df = pd.concat([df, df1])
    return df