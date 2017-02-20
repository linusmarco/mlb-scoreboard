import psycopg2
from sqlalchemy_utils import database_exists, create_database, drop_database

import database.models.base
import database.models.game

import database.utilities.helpers as hlp

def create_db():
    '''
    Creates app database. If database already exists, drops existing
    '''  
    engine = hlp.create_engine()
    if database_exists(engine.url):
        drop_database(engine.url)
        
    create_database(engine.url)

    return engine


def create_tables(engine):
    '''
    Creates tables in database
    '''
    database.models.base.Base.metadata.create_all(engine)


if (__name__ == "__main__"):
    engine = create_db()
    create_tables(engine)
