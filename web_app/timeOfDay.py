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
    post_midnight = datetime.datetime(2000, 1, 1, 00, 00, 00).time()
    morning = datetime.datetime(2000, 1, 1, 04, 00, 00).time()
    late_morning = datetime.datetime(2000, 1, 1, 8, 00, 00).time()
    afternoon = datetime.datetime(2000, 1, 1, 12, 00, 00).time()
    evening = datetime.datetime(2000, 1, 1, 16, 00, 00).time()
    late_evening = datetime.datetime(2000, 1, 1, 20, 00, 00).time()

    post_midnight_count_start = 0
    morning_count_start = 0
    late_morning_count_start = 0
    afternoon_count_start = 0
    evening_count_start = 0
    late_evening_count_start = 0

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

    print type(post_midnight)
    print type(morning)
    print type(late_morning)

    date_series_start = pd.to_datetime(df['start_time1'])
    print len(date_series_start)
    for x in date_series_start:
        if morning > x.time() > post_midnight:
            post_midnight_count_start += 1
        elif late_morning > x.time() > morning:
            morning_count_start += 1
        elif afternoon > x.time() > late_morning:
            late_morning_count_start += 1
        elif evening > x.time() > afternoon:
            afternoon_count_start += 1
        elif late_evening > x.time() > evening:
            evening_count_start += 1
        else:
            late_evening_count_start += 1
    print 'exit for loop start'

    date_series_stop = pd.to_datetime(df['stoptime'])

    df = pd.DataFrame({'Time of Day': ['00-00 - 04-00', '04-00 - 08-00', '08-00 - 12-00', '12-00 - 16-00',
                                       '16-00 - 20-00', '20-00 - 00-00'],
                       'Time': [post_midnight_count_start, morning_count_start, late_morning_count_start,
                                afternoon_count_start, evening_count_start, late_evening_count_start]})
    b = Bar(df, title="Time Of Day", label='Time of Day', values='Time')
    b.left[0].formatter.use_scientific = False
    scriptb, divb = components(b)
    return render_template('timeOfDay.html', d1=date_start, d2=date_stop_jinja2, scriptb=scriptb, divb=divb)
