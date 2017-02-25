import sqlalchemy

import datetime
import re


def create_engine():
    engine = sqlalchemy.create_engine("postgres://localhost/mlb-scoreboard-db")
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
    if (type(val) in [int, float]):
        return int(val)
    elif (type(val) == str):
        if (re.compile(r"^-?\d*$").match(val)):
            if (val == ""):
                return None
            else:
                return int(val)
        else:
            print("WARNING: Could not parse int: {}. Allowing default.".format(val))
            return None
    else:
        raise ValueError("ERROR: Unrecognized type: {}".format(type(val)))


def format_str(val, sql_type):
    try:
        assert(type(val) == str)
        assert(re.compile(r"^VARCHAR\(\d+\)$").match(sql_type).group(0) == sql_type)
        assert(int(re.compile(r"\d+").search(sql_type).group(0)) >= len(val))
    except: 
        print("WARNING: Could not parse {}: {}. Forcing to string.".format(sql_type, val))
        return str(val)
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
