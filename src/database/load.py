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


class MyDialect(csv.Dialect):
    strict = True
    skipinitialspace = True
    quoting = csv.QUOTE_NONNUMERIC
    quotechar = '"'
    delimiter = ','
    lineterminator = '\n'


def load_years(first, last):
    for y in range(first, last + 1):
        file = get_logs(y)
        logs = read_logs(file, game_columns)
        load_logs(logs)

        print("Lodaed {} game logs".format(y))


def get_logs(year):  
    with url.urlopen('http://www.retrosheet.org/gamelogs/gl{}.zip'.format(year)) as r:
        zf = zipfile.ZipFile(BytesIO(r.read()))

        with zf.open("GL{}.TXT".format(year)) as f:
            return f.read()


def read_logs(log, columns):
    l = StringIO(log.decode('ascii'))
    r = csv.DictReader(l, fieldnames=columns, dialect=MyDialect())
    return r


def load_logs(log):
    
    engine = hlp.create_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    games = []
    for row in log:

        game = Game()

        for key, val in row.items():
            
            game.setattr(key, val)

        games.append(game)

        # print("{} - {} @ {}".format(row['Date'], row['VisitingTeam'], row['HomeTeam']))

    session.add_all(games)
    session.commit()


if (__name__ == "__main__"):

    load_years(2015, 2015)

    


