import datetime
from web_app.get_dataframe import get_dataframe
import pandas as pd

def create_df():
    print datetime.datetime.now().time()
    start_time = datetime.datetime.strptime('2013-07-01', "%Y-%m-%d").date()
    stop_time = datetime.datetime.strptime('2013-07-01', "%Y-%m-%d").date()
    dataframe = get_dataframe(start_time, stop_time)
    return dataframe