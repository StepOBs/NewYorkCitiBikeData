import datetime
import pandas as pd
from bokeh.charts import Bar
from bokeh.embed import components
from flask import render_template, request
from web_app.app import app, df_init
from web_app.form_methods import gender_form, date_form, station_form, age_form, time_form
from web_app.get_dataframe import get_dataframe


@app.route('/tripDuration', methods=['GET', 'POST'])
def get_tripduration():
    hour_or_less_count = 0
    day_or_less_count = 0
    halfday_or_less_count = 0
    day_or_more_count = 0

    start_date_range = datetime.datetime.strptime(request.form['start_date'], "%Y-%m-%d").date()
    end_date_jinja2 = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()
    end_date_range = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()

    date_start = str(start_date_range)
    date_stop = str(end_date_range)
    date_stop_jinja2 = str(end_date_jinja2)

    #df = get_dataframe(start_date_range, end_date_range)

    if 'submitDateFilter' in request.form:
        df = date_form(df_init, date_start, date_stop)

    if 'submit_station' in request.form:
        df = station_form(df_init, date_start, date_stop)

    if 'submit_gender' in request.form:
        df = gender_form(df_init, date_start, date_stop)

    if 'submit_age' in request.form:
        df = age_form(df_init, date_start, date_stop)

    if 'submit_time' in request.form:
        df = time_form(df_init, date_start, date_stop)

    df = df_init
    trip_duration_series = df['tripduration'].values

    for x in trip_duration_series:
        x = int(x)
        if x <= 3600:
            hour_or_less_count += 1
        elif x <= 43200:
            halfday_or_less_count += 1
        elif x <= 86400:
            day_or_less_count += 1
        else:
            day_or_more_count += 1
    total = halfday_or_less_count + hour_or_less_count + day_or_more_count + day_or_less_count
    print long(hour_or_less_count)
    if day_or_more_count == 0:
        #durations = [hour_or_less_count, halfday_or_less_count, day_or_less_count]
        df = pd.DataFrame({'Journey Length': ['0-60mins', '1-12hrs', '12-24hrs'],
                           'Durations': [hour_or_less_count, halfday_or_less_count, day_or_less_count]})
    else:
        df = pd.DataFrame({'Journey Length': ['0-60mins', '1-12hrs', '12-24hrs', '24+hrs'],
                           'Durations': [long(hour_or_less_count), long(halfday_or_less_count), long(day_or_less_count),
                                     long(day_or_more_count)]})
        #durations = [hour_or_less_count, halfday_or_less_count, day_or_less_count, day_or_more_count]
    # p = Bar(durations, title="Bar example", xlabel='categories', ylabel='values', width=400, height=400)
    b = Bar(df, title="Journey Lengths", label='Journey Length', values='Durations')
    b.left[0].formatter.use_scientific = False
    scriptb, divb = components(b)
    return render_template('tripDuration.html', p1=hour_or_less_count, p2=halfday_or_less_count, p3=day_or_less_count,
                           p4=day_or_more_count, p5=total, d1=date_start, d2=date_stop_jinja2, scriptb=scriptb,
                           divb=divb)
