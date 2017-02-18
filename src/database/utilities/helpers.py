from sqlalchemy import create_engine


def create_engine():
    engine = create_engine("postgres://localhost/mlb-scoreboard-db", echo=True)
    return engine
