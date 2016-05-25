from flask import Flask
from web_app import dataframe_wrapper

app = Flask(__name__)
app.template_folder = '../templates'
app.static_folder = '../static'
df_init = dataframe_wrapper.create_df()
from web_app import views, heatmap, timeOfDay, gender, age, tripDuration, userType, get_dataframe, dataframe_wrapper
