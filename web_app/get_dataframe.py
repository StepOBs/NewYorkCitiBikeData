import datetime
import sqlite3
import time
import pandas as pd

def get_dataframe(start_date_range, end_date_range):
    print (datetime.datetime.now().time())
    conn = sqlite3.connect('db/bike_data.db')
    db_file = 'newbikes'
    df = pd.read_sql_query("SELECT * from " + db_file, conn)
    print 'read file {}'.format(db_file)
    # #start_date_month = 7
    # start_date_month = start_date_range.month
    # #start_date_year = 2013
    # start_date_year = start_date_range.year
    # end_date_month = end_date_range.month
    # end_date_year = end_date_range.year
    # end_date_range += datetime.timedelta(days=1)
    # now = datetime.datetime.now()
    #
    # if start_date_month < 10:
    #     start_date_month = '0' + str(start_date_month)
    # else:
    #     start_date_month = str(start_date_month)
    # start_date_year = str(start_date_year)
    #
    # if end_date_month < 10:
    #     end_date_month = '0' + str(end_date_month)
    # else:
    #     end_date_month = str(end_date_month)
    # end_date_year = str(end_date_year)
    #
    # if (start_date_month == end_date_month) and (start_date_year == end_date_year):
    #     print 'same month and year'
    #     db_file = 'bikes_{}_{}'.format(start_date_year, start_date_month)
    #     #db_file = 'bikes_{}_{}'.format(start_date_year, start_date_month)
    #     df = pd.read_sql_query("SELECT * from " + db_file, conn)
    # else:
    #     print 'diff month and year'
    #     db_file = 'bikes_{}_{}'.format(start_date_year, start_date_month)
    #     print datetime.datetime.now().time()
    #     df = pd.read_sql_query("SELECT * from " + db_file, conn)
    #     print 'read file {}'.format(db_file)
    #     #while int(start_date_year) != now.year or not (int(start_date_month) == now.month):
    #     #(year == 2016 and month == 3):
    #     while not (int(start_date_year) == int(end_date_year) and int(start_date_month) == int(end_date_month)):
    #         start_date_year = int(start_date_year)
    #         start_date_month = int(start_date_month)
    #
    #         if start_date_month == 12:
    #             start_date_month = 1
    #             start_date_year += 1
    #         else:
    #             start_date_month += 1
    #
    #         if start_date_month < 10:
    #             start_date_month = '0' + str(start_date_month)
    #         else:
    #             start_date_month = str(start_date_month)
    #
    #         if end_date_month < 10:
    #             end_date_month = '0' + str(end_date_month)
    #         else:
    #             end_date_month = str(end_date_month)
    #
    #         db_file = 'bikes_{}_{}'.format(start_date_year, start_date_month)
    #         print 'before read file'
    #         df1 = pd.read_sql_query("SELECT * from " + db_file, conn)
    #         print 'read file {}'.format(db_file)
    #         time.sleep(10)
    #         df = pd.concat([df, df1])
    #         time.sleep(5)
    # print (datetime.datetime.now().time())
    conn.close()
    #time.sleep(5)
    return df