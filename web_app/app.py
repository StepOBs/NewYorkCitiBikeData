from flask import Flask

app = Flask(__name__)
app.template_folder = '../templates'
app.static_folder = '../static'
from web_app import views, heatmap, timeOfDay, gender, age, tripDuration, userType, get_dataframe