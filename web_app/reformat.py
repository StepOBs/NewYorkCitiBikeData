import pandas as pd

def reformat_data(df): #should be able to remove this after data cleaning
    temp_df = pd.Series(df['starttime'])
    b = temp_df.tolist()
    first = str(b[0])
    if (first[1] == '/') or (first[2] == '/'):
        print 'slash'
        #if ((int(start_date_month) >= 9) and (start_date_year >= 2014)) or (start_date_year > 2014):
        temp_df = pd.Series(df['starttime'])
        a = temp_df.tolist()
        length = len(a[0])
        if length > 16:
            df['starttime'] = pd.to_datetime((df['starttime']), format="%m/%d/%Y %H:%M:%S")
        else:
            df['starttime'] = pd.to_datetime((df['starttime']), format="%m/%d/%Y %H:%M")
    return df