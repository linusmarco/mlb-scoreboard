import os

from app import app
from flask import send_from_directory, redirect, url_for


# # main page
# @app.route('/app/index')
# def send_main():
#     return app.send_static_file('index.html')

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
@app.route('/api/<path:path>')
def send_api(path):
    return "API"

# error
# @app.errorhandler(404)
# def page_not_found(e):
#     return redirect(url_for('index'))
