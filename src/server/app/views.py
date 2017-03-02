import os
import json

from server.app import app
from flask import send_from_directory, redirect, url_for

from sqlalchemy.orm import sessionmaker

import server.database.utilities.helpers as hlp
from server.database.models.base import Base
from server.database.models.game import Game


# send app
@app.route('/app/<path:path>')
@app.route('/app/<path:path>/')
def send_app(path):
    return app.send_static_file('index.html')


# main page
@app.route('/')
def index():
    return redirect(url_for('send_app', path="index"))


# api
@app.route('/api/games/date/<int:date>')
def send_games_by_date(date):
    try:
        dt = hlp.format_date(str(date))
    except:
        return "ERROR: INVALID DATE", 400
    else:
        engine = hlp.create_engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        res = session.query(Game).filter(Game.Date == dt).all()
        d = [x.to_dict() for x in res]
        return json.dumps(d)

