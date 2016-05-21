import datetime
import pandas as pd
from bokeh.charts import Bar
from bokeh.embed import components
from flask import render_template, request
from web_app.app import app
from web_app.form_methods import gender_form, date_form, station_form, time_form
from web_app.get_dataframe import get_dataframe

@app.route('/age', methods=['GET', 'POST'])
def get_age():
    # conn = sqlite3.connect('bike_data.db')
    # print "Opened database successfully"
    # df2 = pd.read_sql_query("SELECT * from bikes_2013_07", conn)
    # print "Connected to table {}".format("2013_07")
    # print df2['tripduration']

    # print df2['starttime']
    child_count = 0
    young_adult_count = 0
    mid_age_count = 0
    oap_count = 0
    null = 0
    now = datetime.datetime.now()
    year = now.year
    start_date_range = datetime.datetime.strptime(request.form['start_date'], "%Y-%m-%d").date()
    end_date_jinja2 = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()
    end_date_range = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()

    date_start = str(start_date_range)
    date_stop = str(end_date_range)
    date_stop_jinja2 = str(end_date_jinja2)

    df = get_dataframe(start_date_range, end_date_range)
    # print date_start
    # print date_stop
    if 'submitDateFilter' in request.form:
        df = date_form(df, date_start, date_stop)

    if 'submit_station' in request.form:
        df = station_form(df, date_start, date_stop)

    if 'submit_gender' in request.form:
        df = gender_form(df, date_start, date_stop)

    if 'submit_time' in request.form:
        df = time_form(df, date_start, date_stop)

    age_series = df['birth_year'].values
    #print type(age_series[0])
    for x in age_series:
        x = str(x)
        if (x != '\N') and (x != '') and (x != 'NaN') and (x != 'nan'):
            x = round(float(x))
            #x = round(x)
            if type(x) is not int:
                x = int(x)
            if year - x <= 30:
                young_adult_count += 1
            elif year - x <= 65:
                mid_age_count += 1
            else:
                oap_count += 1
        else:
            null += 1
    total = child_count + young_adult_count + mid_age_count + oap_count + null
    if null == 0:
        #ages = [young_adult_count, mid_age_count, oap_count]
        df = pd.DataFrame({'Age': ['16-30', '31-65', '65+'],
                           'Age Group': [young_adult_count, mid_age_count, oap_count]})
    else:
        #ages = [young_adult_count, mid_age_count, oap_count, null]
        df = pd.DataFrame({'Age': ['16-30', '31-65', '65+', 'Unknown'],
                           'Age Group': [young_adult_count, mid_age_count, oap_count, null]})
    b = Bar(df, title="Age", label='Age', values='Age Group')
    b.left[0].formatter.use_scientific = False
    scriptb, divb = components(b)
    return render_template('age.html', n=null, c=child_count, y=young_adult_count,
                           m=mid_age_count, o=oap_count, t=total, d1=date_start,
                           d2=date_stop_jinja2, scriptb=scriptb, divb=divb)