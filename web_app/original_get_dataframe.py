import datetime
import sqlite3
import time

import pandas as pd


def get_dataframe(start_date_range, end_date_range):
    conn = sqlite3.connect('bike_data.db')
    start_date_month = start_date_range.month
    start_date_year = start_date_range.year

    end_date_month = end_date_range.month
    end_date_year = end_date_range.year

    end_date_range += datetime.timedelta(days=1)

    if start_date_month < 10:
        start_date_month = '0' + str(start_date_month)
    else:
        start_date_month = str(start_date_month)

    start_date_year = str(start_date_year)

    if end_date_month < 10:
        end_date_month = '0' + str(end_date_month)
    else:
        end_date_month= str(end_date_month)

    end_date_year = str(end_date_year)

    if (start_date_month == end_date_month) and (start_date_year == end_date_year):
        print 'same month and year'
        db_file = 'bikes_{}_{}'.format(start_date_year, start_date_month)
        df = pd.read_sql_query("SELECT * from " + db_file , conn)

        #df = pd.read_csv("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + start_date_year + "-" + start_date_month +
        #             " - Citi Bike trip data.csv", sep=",")
        # #print "/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + start_date_year + "-" + start_date_month +\
        #       #" - Citi Bike trip data.csv"
        # if ((int(start_date_month) >= 9) and (start_date_year >= 2014)) or (start_date_year > 2014):
        #     temp_df = pd.Series(df['starttime'])
        #     a= temp_df.tolist()
        #     length = len(a[0])
        #     if length <=16:
        #         #print 'less than 1'
        #         df['starttime'] = pd.to_datetime((df['starttime']), format = "%m/%d/%Y %H:%M")
        #         #print (df['starttime'])
        #     else:
        #         df['starttime'] = pd.to_datetime((df['starttime']), format = "%m/%d/%Y %H:%M:%S")
        #     #print (df['starttime'])
    else:
        print 'diff month and year'
        db_file = 'bikes_{}_{}'.format(start_date_year, start_date_month)
        df = pd.read_sql_query("SELECT * from " + db_file , conn)
        print 'read file {}'.format(db_file)
        #df = pd.read_csv("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + start_date_year + "-" + start_date_month +
        #             " - Citi Bike trip data.csv", sep=",")
        #print (df['starttime'])
        #print "/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + start_date_year + "-" + start_date_month +\
              #" - Citi Bike trip data.csv"

        #df = reformat_data(df)

        while int(start_date_year) != int(end_date_year) or not (int(start_date_month) == int(end_date_month)):
            print 'enter while'
            start_date_year = int(start_date_year)
            start_date_month = int(start_date_month)
            if start_date_month == 12:
                print 'in if 1'
                start_date_month = 1
                start_date_year += 1
            else:
                print 'in else 1'
                start_date_month += 1
            if start_date_month < 10:
                print 'in if 2'
                start_date_month = '0' + str(start_date_month)
            else:
                print 'in else 2'
                start_date_month = str(start_date_month)

            if end_date_month < 10:
                print 'in if 3'
                end_date_month = '0' + str(end_date_month)
            else:
                print 'in else 3'
                end_date_month = str(end_date_month)

            db_file = 'bikes_{}_{}'.format(start_date_year, start_date_month)
            print 'before read file'
            df1 = pd.read_sql_query("SELECT * from " + db_file , conn)

            #df1 = pd.read_csv("/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + str(start_date_year) + "-" + start_date_month +
            #         " - Citi Bike trip data.csv", sep=",")
            print 'read file {}'.format(db_file)
            #print "/home/stephen/Documents/College/4th Year/4th Year Project/BikeData/" + str(start_date_year) + "-" + start_date_month + \
                  #" - Citi Bike trip data.csv"

            #df1 = reformat_data(df1)
            df = pd.concat([df, df1])
            time.sleep(5)
            print 'end while'
        print 'exit while'

        # print 'printing df'
        # print (df['starttime'])
        # print 'printed df'
        # print 'exit while'
    #print df['starttime']
    return df