import datetime
import pandas as pd

from bokeh.embed import components
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle,\
    DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
from flask import render_template, request
from web_app.app import app
from web_app.get_dataframe import get_dataframe


@app.route('/heatmap', methods=['GET', 'POST'])
def generate_heatmap():
    #take date range from user input
    start_date_range = datetime.datetime.strptime(request.form['start_date'],
                                                  "%Y-%m-%d").date()
    end_date_range = datetime.datetime.strptime(request.form['stop_date'],
                                                "%Y-%m-%d").date()

    #calls method to get Pandas data frame within given date range.
    df = get_dataframe(start_date_range, end_date_range)

    #reads the data frame and stores the latitudes and longitudes for the
    #start stations and the end stations
    start_lats = pd.Series(df['start_station_latitude']).unique()
    start_long = pd.Series(df['start_station_longitude']).unique()

    small_occurrences = []
    occurrences = df['start_station_latitude'].value_counts(sort=False)
    minimum = min(occurrences)
    print 'max:'
    print (max(occurrences))

    #scaling to ensure 'blobs' will always be viewable on the map of NYC
    for o in occurrences:
        o /= (minimum * 2)
        small_occurrences.append(o)

    #Maps out an area of NYC based on the coordinates. Zoom=12 giving issue
    map_options = GMapOptions(lat=40.741557, lng=-73.990467, map_type="roadmap", zoom=11)

    #set the data to displayed on the map: latitudes, longitudes and occurences
    plot = GMapPlot(
        x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="NYC Baby"
    )
    source = ColumnDataSource(
        data=dict(
            lat=start_lats,
            lon=start_long,
            sizes=small_occurrences,
        ))

    #choose the type of shape to plot, size is set to the number of occurrences
    circle = Circle(x="lon", y="lat", size='sizes', fill_color="blue", fill_alpha=1.8, line_color=None)

    #adding the plot and tools to the plot
    plot.add_glyph(source, circle)
    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

    #return to the template
    scriptb, divb = components(plot)
    return render_template('heatmap.html', d1=start_date_range, d2=end_date_range, scriptb=scriptb, divb=divb)