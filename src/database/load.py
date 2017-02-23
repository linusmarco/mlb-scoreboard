import sys

import urllib.request as url

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import database.utilities.helpers as hlp

from database.models.base import Base
from database.models.game import Game, game_columns

import datetime

import csv
from io import BytesIO, StringIO

import zipfile


def load_years(first, last):
    for y in range(first, last + 1):
        file = get_logs(y)
        logs = read_logs(file, game_columns)
        games = prepare_logs(logs)
        load_games(games)

        print("Loaded {} ({} games)".format(y, len(games)))


def get_logs(year):  
    with url.urlopen('http://www.retrosheet.org/gamelogs/gl{}.zip'.format(year)) as r:
        zf = zipfile.ZipFile(BytesIO(r.read()))

        with zf.open("GL{}.TXT".format(year)) as f:
            return f.read()


def read_logs(log, columns):
    logs_file = StringIO(log.decode('ascii'))
    reader = csv.DictReader(logs_file.readlines(), columns)
    return reader


def prepare_logs(log):
    games = []
    for row in log:
        game = Game()
        for key, val in row.items():
            game.setattr(key, val)
        games.append(game)
    return games


def load_games(games):
    engine = hlp.create_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all(games)
    session.commit()


if (__name__ == "__main__"):
    load_years(1871, 2016)

    


