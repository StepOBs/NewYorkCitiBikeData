from flask import render_template
from web_app.get_dataframe import get_dataframe
from web_app.app import app
import datetime

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/date_search', methods=['GET', 'POST'])
def date_search():
    return render_template("search_by_date.html")

@app.route('/station_search', methods=['GET', 'POST'])
def station_search():
    return render_template("search_by_station.html")

@app.route('/gender_search', methods=['GET', 'POST'])
def gender_search():
    return render_template("search_by_gender.html")

@app.route('/age_search', methods=['GET', 'POST'])
def age_search():
    return render_template("search_by_age.html")

@app.route('/time_of_day_search', methods=['GET', 'POST'])
def time_of_day_search():
    return render_template("search_by_time_of_day.html")