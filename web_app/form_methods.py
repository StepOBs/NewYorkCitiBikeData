import datetime
import pandas as pd
from datetime import date
from flask import request

def date_form(df, date_start, date_stop):
    if df['starttime'].dtype == object: #removed redundant parentheses
        df['starttime'] = pd.to_datetime(df['starttime'])
    df.index.name = 'starttime'
    df = df.set_index(['starttime'])
    df = df.loc[date_start:date_stop]
    return df

def station_form(df, date_start, date_stop):
    if df['starttime'].dtype == object:
        df['starttime'] = pd.to_datetime(df['starttime'])

    df = df.set_index(['starttime'])
    df = df.loc[date_start:date_stop]
    start_station = request.form['start_Station']
    stop_station = request.form['stop_Station']

    print start_station
    print stop_station
    if start_station == "":
        df = df[df['end_station_name'] == stop_station]
    elif stop_station == "":
        df = df[df['start_station_name'] == start_station]
    else:
        df = df[(df['start_station_name'] == start_station) & (df['end_station_name'] == stop_station)]
    return df

def gender_form(df, date_start, date_stop):

    #if df['starttime'].dtype == object:
        #print 'changing type'
    df['starttime'] = pd.to_datetime(df['starttime'])

    df = df.set_index(['starttime'])
    df = df.loc[date_start:date_stop]

    gender = request.form['gender']
    print gender
    if gender == 'male':
        gender = 1
    elif gender == 'female':
        gender = 2
    else:
        gender = 3
    df['gender'] = pd.to_numeric(df['gender'])
    print df['gender'].dtype
    df = df[df['gender'] == gender]
    return df

def age_form(df, date_start, date_stop):
    if df['starttime'].dtype == object:
        #print 'changing type'
        df['starttime'] = pd.to_datetime(df['starttime'])
    df = df.set_index(['starttime'])
    df = df.loc[date_start:date_stop]

    min_age = request.form['start_age']
    max_age = request.form['stop_age']

    df = df[(df['birth_year'] != '') & (df['birth_year'] != '\N')]
    df['birth_year'] = df['birth_year']
    df['birth_year'] = pd.to_numeric(df['birth_year'])
    if min_age == "":
        max_age_year = date.today().year - int(max_age)
        df = df[df['birth_year'] >= int(max_age_year)]
    elif max_age == "":
        min_age_year = date.today().year - int(min_age)
        df = df[df['birth_year'] <= int(min_age_year)]
    else:
        min_age_year = date.today().year - int(min_age)
        max_age_year = date.today().year - int(max_age)
        df = df[(df['birth_year'] >= int(max_age_year)) & (df['birth_year'] <= int(min_age_year))]
    return df

def time_form(df, date_start, date_stop):
    #if df['starttime'].dtype == object:
    df['starttime'] = pd.to_datetime(df['starttime'])
    print
    df = df.set_index(['starttime'])
    df = df.loc[date_start:date_stop]
    df = df.reset_index()
    temp_df = pd.Series(df['starttime'])
    a = temp_df.tolist()
    date_array = []
    for single_date in a:
        date_array.append(datetime.datetime.strptime(str(single_date), "%Y-%m-%d %H:%M:%S").time())
    ds = pd.DataFrame(date_array)
    ds.columns = ['time']
    pd.to_datetime(ds['time'], format='%H:%M:%S')
    df['starttime'] = ds['time']
    start_time = datetime.datetime.strptime(request.form['start_time'], "%H:%M").time()
    start_time = start_time.replace(second=0)
    end_time = datetime.datetime.strptime(request.form['end_time'], "%H:%M").time()
    end_time = end_time.replace(second=0)
    df = df.set_index(['starttime'])
    df = df.loc[start_time:end_time]
    df = df.reset_index()
    return df
