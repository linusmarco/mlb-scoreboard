import sqlalchemy

import datetime
import re


def create_engine():
    engine = sqlalchemy.create_engine("postgres://localhost/mlb-scoreboard-db", echo=True)
    return engine


def format_date(val):
    try:
        assert type(val) == str
        assert len(val) == 8
        assert 1850 <= int(val[:4]) <= datetime.datetime.now().year 
        assert 1 <= int(val[4:6]) <= 12
        assert 1 <= int(val[6:8]) <= 31
    except:
        raise ValueError("ERROR: Could not parse date: {}".format(val))
    else:
        return datetime.datetime.strptime(val, "%Y%m%d").date()


def format_int(val):
    try:
        assert type(val) in [int, float]
        assert round(val) == val
    except: 
        raise ValueError("ERROR: Could not parse int: {}".format(val))
    else:
        return int(val)


def format_str(val, sql_type):
    try:
        assert(type(val) == str)
        assert(re.compile(r"^VARCHAR\(\d+\)$").match(sql_type).group(0) == sql_type)
        assert(int(re.compile(r"\d+").search(sql_type).group(0)) >= len(val))
    except: 
        raise ValueError("ERROR: Could not parse {}: {}".format(sql_type, val))
    else:
        return val


def format_val(val, sql_type):

    if (sql_type == "DATE"):
        val_fmt = format_date(val)

    elif (sql_type == "INTEGER"):
        val_fmt = format_int(val)

    elif (sql_type.startswith("VARCHAR")):
        val_fmt = format_str(val, sql_type)

    else:
        raise ValueError("ERROR: Unrecognized type: {}".format(sql_type))

    return val_fmt
