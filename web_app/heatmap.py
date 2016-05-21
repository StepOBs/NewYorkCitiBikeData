import datetime
import pandas as pd

from bokeh.embed import components
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool,\
    WheelZoomTool, BoxSelectTool, HoverTool
from flask import render_template, request
from web_app.app import app
from web_app.get_dataframe import get_dataframe


@app.route('/heatmap', methods=['GET', 'POST'])
def generate_heatmap():
    start_date_range = datetime.datetime.strptime(request.form['start_date'], "%Y-%m-%d").date()
    end_date_range = datetime.datetime.strptime(request.form['stop_date'], "%Y-%m-%d").date()

    df = get_dataframe(start_date_range, end_date_range)

    start_lats = pd.Series(df['start_station_latitude']).unique()
    stop_lats = pd.Series(df['end_station_latitude']).unique()
    start_long = pd.Series(df['start_station_longitude']).unique()
    stop_long = pd.Series(df['end_station_longitude']).unique()

    small_occurrences = []
    occurrences = df['start_station_latitude'].value_counts(sort=False)
    for o in occurrences:
        o /= 200
        small_occurrences.append(o)

    for o in small_occurrences:
        print o

    lats = start_lats.tolist() + stop_lats.tolist()
    longs = start_long.tolist() + stop_long.tolist()

    map_options = GMapOptions(lat=40.741557, lng=-73.990467, map_type="roadmap", zoom=11)
    plot = GMapPlot(
        x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="NYC Baby"
    )
    source = ColumnDataSource(
        data=dict(
            lat=lats,
            lon=longs,
            sizes=small_occurrences,
        )
    )

    circle = Circle(x="lon", y="lat", size='sizes', fill_color="blue", fill_alpha=1.8, line_color=None)
    plot.add_glyph(source, circle)
    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), HoverTool())
    script, div = components(plot)
    return render_template('heatmap.html', script=script, div=div)