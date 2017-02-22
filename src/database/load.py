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
        logs = read_logs(file)
        load_logs(logs, game_columns)

        print("Loaded {} game logs".format(y))


def get_logs(year):  
    with url.urlopen('http://www.retrosheet.org/gamelogs/gl{}.zip'.format(year)) as r:
        zf = zipfile.ZipFile(BytesIO(r.read()))

        with zf.open("GL{}.TXT".format(year)) as f:
            return f.read()


def read_logs(log):
    l = StringIO(log.decode('ascii'))
    return l.readlines()


def parse_line(line, columns):
    # if line.endswith("\r\n"):
    #     line = line[:-2]
    # elif line.endswith("\n"):
    #     line = line[:-1]

    # vals = line.split(',')

    # try:
    #     assert len(vals) == len(columns)
    # except:
    #     print(vals)
    #     assert 0

    # d = {}
    # for col, val in zip(columns, vals):
    #     if (val.startswith('"') and val.endswith('"')):
    #         val = val[1:-1]
    #     d[col] = val

    d = csv.DictReader(StringIO(line), fieldnames=columns)

    return list(d)[0]


def load_logs(log, columns):
    
    games = []
    for row in log:
        l = parse_line(row, columns)

        game = Game()

        for key, val in l.items():
            
            game.setattr(key, val)

        games.append(game)

        # print("{} - {} @ {}".format(row['Date'], row['VisitingTeam'], row['HomeTeam']))

    engine = hlp.create_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all(games)
    session.commit()


if (__name__ == "__main__"):

    load_years(1871, 1915)

    


