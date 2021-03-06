import datetime

import pandas as pd
from bokeh.charts import Bar
from bokeh.embed import components
from bokeh.models import HoverTool, GlyphRenderer
from flask import render_template, request

from web_app.app import app, df_init
from web_app.form_methods import gender_form, date_form, station_form, age_form, time_form
from web_app.get_dataframe import get_dataframe


@app.route('/userType', methods=['GET', 'POST'])
def get_user_type():
    subscriber_count = 0
    customer_count = 0
    unknown_count = 0

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
    user_type_series = df['usertype'].values

    for x in user_type_series:
        if x == 'Subscriber':
            subscriber_count += 1
        elif x == 'Customer':
            customer_count += 1
        else:
            unknown_count += 1
    if unknown_count == 0:
        #customer_type = [subscriber_count, customer_count]
        df = pd.DataFrame({'User Type': ['Subscriber', 'Customer'],
                           'Type': [subscriber_count, customer_count]})
    else:
        #customer_type = [subscriber_count, customer_count, unknown_count]
        df = pd.DataFrame({'User Type': ['Subscriber', 'Customer', 'Null'],
                           'Type': [subscriber_count, customer_count, unknown_count]})
    #b = Bar(customer_type, title="Bar example", label='categories', ylabel='values', width=400, height=400)
    b = Bar(df, title="User Types", label='User Type', values='Type')
    b.select(dict(type=GlyphRenderer))
    b.left[0].formatter.use_scientific = False
    scriptb, divb = components(b)
    return render_template('userType.html', s=subscriber_count, c=customer_count, u=unknown_count,
                           d1=date_start, d2=date_stop_jinja2, scriptb=scriptb, divb=divb)
