from flask import render_template

from web_app.app import app

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")