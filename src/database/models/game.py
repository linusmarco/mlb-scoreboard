from sqlalchemy import *
from .base import Base

class Game(Base):
    __tablename__ = 'games'

    date = Column(Date, primary_key=True)
    visitor = Column(String(3), primary_key=True)
    home = Column(String(3), primary_key=True)
    game_number = Column(String(1), primary_key=True)
    visitor_score = Column(Integer)
    home_score = Column(Integer)

    def __repr__(self):
       return "<Game(home='%s', away='%s')>" % (
                self.home, self.visitor)