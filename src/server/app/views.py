import os
import json

from app import app
from flask import send_from_directory, redirect, url_for

FAKE_DATA = [
    {
        "id" : 0,
        "name": "Data Element 1",
        "attr_1": "Value 1",
        "attr_2": 15
    },
    {
        "id" : 1,
        "name": "Data Element 2",
        "attr_1": "Value 2",
        "attr_2": 14
    },
    {
        "id" : 2,
        "name": "Data Element 3",
        "attr_1": "Value 3",
        "attr_2": 13
    },
    {
        "id" : 3,
        "name": "Data Element 4",
        "attr_1": "Value 4",
        "attr_2": 12
    }
]

# send app
@app.route('/app/<path:path>')
@app.route('/app/<path:path>/')
def send_app(path):
    return app.send_static_file('index.html')

# main page
@app.route('/')
def index():
    # print(url_for('/app/index'))
    return redirect(url_for('send_app', path="index"))

# api
@app.route('/api/data')
def send_data():
    return json.dumps(FAKE_DATA)

@app.route('/api/datum/<path:id>')
def send_datum(id):
    ids = [d['id'] for d in FAKE_DATA]
    if id.isdigit():
        if(int(id) in ids):
            for d in FAKE_DATA:
                if (d['id'] == int(id)):
                    return json.dumps(d)

    return "", 400
