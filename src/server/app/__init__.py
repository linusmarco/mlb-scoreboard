import os
from flask import Flask

import server.config.default

STATIC_PATH = os.path.abspath('../dist')

app = Flask(__name__, static_url_path='', static_folder=STATIC_PATH)

# Load the default configuration
app.config.from_object('server.config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('../instance/config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')

from server.app import views