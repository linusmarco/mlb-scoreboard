import psycopg2
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database


def create_db():
    '''
    Creates app database. If database already exists, drops existing
    '''  
    engine = create_engine("postgres://localhost/mlb-scoreboard-db")
    if database_exists(engine.url):
        drop_database(engine.url)
        
    create_database(engine.url)


def create_tables():
    '''
    Creates tables in database
    '''
    Base.metadata.create_all(engine)


if (__name__ == "__main__"):
    create_db()
    create_tables()
