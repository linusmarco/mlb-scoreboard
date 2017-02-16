from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.game import Game

import datetime


if (__name__ == "__main__"):

    engine = create_engine("postgres://localhost/mlb-scoreboard-db", echo=True)

    game1 = Game(date=datetime.date.today(),
                 visitor="BOS",
                 home="NYY",
                 game_number="1",
                 visitor_score=0,
                 home_score=10)


    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(game1)

    session.commit()

    print(game1)
