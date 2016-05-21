import datetime
import pandas as pd
from bokeh.charts import Bar
from bokeh.embed import components
from flask import render_template, request
from web_app.app import app
from web_app.form_methods import date_form, station_form, age_form, time_form
from web_app.get_dataframe import get_dataframe


@app.route('/gender', methods=['GET', 'POST'])
def get_gender():
    male_count = 0
    female_count = 0
    gender_unknown = 0

    start_date_range = datetime.datetime.strptime(request.form['start_date'], "%Y-%m-%d").date()
    end_date_jinja2 = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()
    end_date_range = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()

    date_start = str(start_date_range)
    date_stop = str(end_date_range)
    date_stop_jinja2 = str(end_date_jinja2)

    df = get_dataframe(start_date_range, end_date_range)

    if 'submitDateFilter' in request.form:
        df = date_form(df, date_start, date_stop)

    if 'submit_station' in request.form:
        df = station_form(df, date_start, date_stop)

    if 'submit_age' in request.form:
        df = age_form(df, date_start, date_stop)

    if 'submit_time' in request.form:
        df = time_form(df, date_start, date_stop)

    gender_series = df['gender'].values

    for x in gender_series:
        x = int(x)
        if x == 1:
            male_count += 1
        elif x == 2:
            female_count += 1
        else:
            gender_unknown += 1
    total = male_count + female_count + gender_unknown
    if gender_unknown == 0:
        #genders = [male_count, female_count]
        df = pd.DataFrame({'Genders': ['Male', 'Female'],
                           'Gender': [male_count, female_count]})
    else:
        df = pd.DataFrame({'Genders': ['Male', 'Female', 'Unknown'],
                           'Gender': [male_count, female_count, gender_unknown]})
    b = Bar(df, title="Gender", label='Genders', values='Gender')
    b.left[0].formatter.use_scientific = False
    scriptb, divb = components(b)
    return render_template('gender.html', m=male_count, f=female_count, gu=gender_unknown, t=total,
                           d1=date_start, d2=date_stop_jinja2, scriptb=scriptb, divb=divb)