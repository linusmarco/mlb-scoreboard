import os
from flask import Flask

STATIC_PATH = os.path.abspath('../../dist')

app = Flask(__name__, static_url_path='', static_folder=STATIC_PATH)
from app import views