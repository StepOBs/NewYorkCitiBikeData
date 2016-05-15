import datetime
import pandas as pd

from bokeh.charts import Bar
from bokeh.embed import components
from flask import render_template, request
from web_app.app import app
from web_app.form_methods import gender_form, date_form, station_form, age_form
from web_app.get_dataframe import get_dataframe

@app.route('/timeOfDay', methods=['GET', 'POST'])
def get_time_of_day():
    morning = datetime.datetime(2000, 1, 1, 00, 00, 00).time()
    daytime = datetime.datetime(2000, 1, 1, 8, 00, 00).time()
    evening = datetime.datetime(2000, 1, 1, 16, 00, 00).time()

    morning_count_start = 0
    day_count_start = 0
    evening_count_start = 0

    morning_count_stop = 0
    day_count_stop = 0
    evening_count_stop = 0

    start_date_range = datetime.datetime.strptime(request.form['start_date'], "%Y-%m-%d").date()
    end_date_jinja2 = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()
    end_date_range = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()

    date_start = str(start_date_range)
    date_stop = str(end_date_range)
    date_stop_jinja2 = str(end_date_jinja2)
    df = get_dataframe(start_date_range, end_date_range)
    df['start_time1'] = df['starttime']
    if 'submitDateFilter' in request.form:
        print ' in filter'
        df = date_form(df, date_start, date_stop)
    if 'submit_station' in request.form:
        df = station_form(df, date_start, date_stop)

    if 'submit_gender' in request.form:
        df = gender_form(df, date_start, date_stop)

    if 'submit_age' in request.form:
        df = age_form(df, date_start, date_stop)

    date_series_start = pd.to_datetime(df['start_time1'])
    for x in date_series_start:
        if daytime > x.time() > morning:
            morning_count_start += 1
        if evening > x.time() > daytime:
            day_count_start += 1
        else:
            evening_count_start += 1
    print 'exit for loop start'

    date_series_stop = pd.to_datetime(df['stoptime'])

    print 'entering for loop stop'
    for x in date_series_stop:
        print 'in for loop stop'
        if daytime > x.time() > morning:
            morning_count_stop += 1
        if evening > x.time() > daytime:
            day_count_stop += 1
        else:
            evening_count_stop += 1
    print 'exit for loop stop'

    total = morning_count_stop + day_count_stop + evening_count_stop
    times = [morning_count_start, day_count_start, evening_count_start]
    p = Bar(times, title="Journeys per time of day", ylabel='No. of Trips', width=400, height=400)
    script, div = components(p)
    return render_template('timeOfDay.html', t=total, d1=date_start, d2=date_stop_jinja2, script=script, div=div)