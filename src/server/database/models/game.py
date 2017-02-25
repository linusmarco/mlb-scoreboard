from sqlalchemy import *
from .base import Base

from server.database.utilities import helpers as hlp

import datetime

class Game(Base):
    __tablename__ = 'games'

    Date = Column(Date, primary_key=True, nullable=False, default=datetime.date(3000, 1, 1))

    DoubleHeader = Column(String(1), primary_key=True, nullable=False)
    DayOfWeek    = Column(String(3), nullable=False)
    
    VisitingTeam           = Column(String(3), primary_key=True, nullable=False)
    VisitingTeamLeague     = Column(String(2), nullable=False)
    VisitingTeamGameNumber = Column(Integer, nullable=False, default=0)
    HomeTeam               = Column(String(3), primary_key=True, nullable=False)
    HomeTeamLeague         = Column(String(2), nullable=False)
    HomeTeamGameNumber     = Column(Integer, nullable=False, default=0)

    VisitorRunsScored = Column(Integer, nullable=False, default=0)
    HomeRunsScored    = Column(Integer, nullable=False, default=0)
    
    LengthInOuts = Column(Integer, nullable=False, default=0)
    
    DayNight = Column(String(1), nullable=False)
    
    CompletionInfo = Column(String(255), nullable=False)
    ForfeitInfo    = Column(String(1), nullable=False)
    ProtestInfo    = Column(String(2), nullable=False)
    
    ParkID     = Column(String(5), nullable=False)
    Attendance = Column(Integer, nullable=False, default=0)
    
    Duration = Column(Integer, nullable=False, default=0)
    
    VisitorLineScore = Column(String(255), nullable=False)
    HomeLineScore    = Column(String(255), nullable=False)
    
    VisitorAB       = Column(Integer, nullable=False, default=0)
    VisitorH        = Column(Integer, nullable=False, default=0)
    Visitor2B       = Column(Integer, nullable=False, default=0)
    Visitor3B       = Column(Integer, nullable=False, default=0)
    VisitorHR       = Column(Integer, nullable=False, default=0)
    VisitorRBI      = Column(Integer, nullable=False, default=0)
    VisitorSH       = Column(Integer, nullable=False, default=0)
    VisitorSF       = Column(Integer, nullable=False, default=0)
    VisitorHBP      = Column(Integer, nullable=False, default=0)
    VisitorBB       = Column(Integer, nullable=False, default=0)
    VisitorIBB      = Column(Integer, nullable=False, default=0)
    VisitorK        = Column(Integer, nullable=False, default=0)
    VisitorSB       = Column(Integer, nullable=False, default=0)
    VisitorCS       = Column(Integer, nullable=False, default=0)
    VisitorGIDP     = Column(Integer, nullable=False, default=0)
    VisitorCI       = Column(Integer, nullable=False, default=0)
    VisitorLOB      = Column(Integer, nullable=False, default=0)
    VisitorPitchers = Column(Integer, nullable=False, default=0)
    VisitorER       = Column(Integer, nullable=False, default=0)
    VisitorTER      = Column(Integer, nullable=False, default=0)
    VisitorWP       = Column(Integer, nullable=False, default=0)
    VisitorBalks    = Column(Integer, nullable=False, default=0)
    VisitorPO       = Column(Integer, nullable=False, default=0)
    VisitorA        = Column(Integer, nullable=False, default=0)
    VisitorE        = Column(Integer, nullable=False, default=0)
    VisitorPB       = Column(Integer, nullable=False, default=0)
    VisitorDP       = Column(Integer, nullable=False, default=0)
    VisitorTP       = Column(Integer, nullable=False, default=0)
    
    HomeAB       = Column(Integer, nullable=False, default=0)
    HomeH        = Column(Integer, nullable=False, default=0)
    Home2B       = Column(Integer, nullable=False, default=0)
    Home3B       = Column(Integer, nullable=False, default=0)
    HomeHR       = Column(Integer, nullable=False, default=0)
    HomeRBI      = Column(Integer, nullable=False, default=0)
    HomeSH       = Column(Integer, nullable=False, default=0)
    HomeSF       = Column(Integer, nullable=False, default=0)
    HomeHBP      = Column(Integer, nullable=False, default=0)
    HomeBB       = Column(Integer, nullable=False, default=0)
    HomeIBB      = Column(Integer, nullable=False, default=0)
    HomeK        = Column(Integer, nullable=False, default=0)
    HomeSB       = Column(Integer, nullable=False, default=0)
    HomeCS       = Column(Integer, nullable=False, default=0)
    HomeGIDP     = Column(Integer, nullable=False, default=0)
    HomeCI       = Column(Integer, nullable=False, default=0)
    HomeLOB      = Column(Integer, nullable=False, default=0)
    HomePitchers = Column(Integer, nullable=False, default=0)
    HomeER       = Column(Integer, nullable=False, default=0)
    HomeTER      = Column(Integer, nullable=False, default=0)
    HomeWP       = Column(Integer, nullable=False, default=0)
    HomeBalks    = Column(Integer, nullable=False, default=0)
    HomePO       = Column(Integer, nullable=False, default=0)
    HomeA        = Column(Integer, nullable=False, default=0)
    HomeE        = Column(Integer, nullable=False, default=0)
    HomePB       = Column(Integer, nullable=False, default=0)
    HomeDP       = Column(Integer, nullable=False, default=0)
    HomeTP       = Column(Integer, nullable=False, default=0)

    UmpireHID     = Column(String(8), nullable=False)
    UmpireHName   = Column(String(255), nullable=False)
    Umpire1BID    = Column(String(8), nullable=False)
    Umpire1BName  = Column(String(255), nullable=False)
    Umpire2BID    = Column(String(8), nullable=False)
    Umpire2BName  = Column(String(255), nullable=False)
    Umpire3BID    = Column(String(8), nullable=False)
    Umpire3BName  = Column(String(255), nullable=False)
    UmpireLFID    = Column(String(8), nullable=False)
    UmpireLFName  = Column(String(255), nullable=False)
    UmpireRFID    = Column(String(8), nullable=False)
    UmpireRFName  = Column(String(255), nullable=False)
    
    VisitorManagerID   = Column(String(8), nullable=False)
    VisitorManagerName = Column(String(255), nullable=False)
    HomeManagerID      = Column(String(8), nullable=False)
    HomeManagerName    = Column(String(255), nullable=False)
    
    VisitorStartingPitcherID   = Column(String(8), nullable=False)
    VisitorStartingPitcherName = Column(String(255), nullable=False)
    HomeStartingPitcherID      = Column(String(8), nullable=False)
    HomeStartingPitcherName    = Column(String(255), nullable=False)

    WinningPitcherID   = Column(String(8), nullable=False)
    WinningPitcherName = Column(String(255), nullable=False)
    LosingPitcherID    = Column(String(8), nullable=False)
    LosingPitcherName  = Column(String(255), nullable=False)
    SavingPitcherID    = Column(String(8), nullable=False)
    SavingPitcherName  = Column(String(255), nullable=False)
    
    GameWinningRBIID   = Column(String(8), nullable=False)
    GameWinningRBIName = Column(String(255), nullable=False)
    
    VisitorBatter1ID       = Column(String(8), nullable=False)
    VisitorBatter1Name     = Column(String(255), nullable=False)
    VisitorBatter1Position = Column(Integer, nullable=False, default=0)
    VisitorBatter2ID       = Column(String(8), nullable=False)
    VisitorBatter2Name     = Column(String(255), nullable=False)
    VisitorBatter2Position = Column(Integer, nullable=False, default=0)
    VisitorBatter3ID       = Column(String(8), nullable=False)
    VisitorBatter3Name     = Column(String(255), nullable=False)
    VisitorBatter3Position = Column(Integer, nullable=False, default=0)
    VisitorBatter4ID       = Column(String(8), nullable=False)
    VisitorBatter4Name     = Column(String(255), nullable=False)
    VisitorBatter4Position = Column(Integer, nullable=False, default=0)
    VisitorBatter5ID       = Column(String(8), nullable=False)
    VisitorBatter5Name     = Column(String(255), nullable=False)
    VisitorBatter5Position = Column(Integer, nullable=False, default=0)
    VisitorBatter6ID       = Column(String(8), nullable=False)
    VisitorBatter6Name     = Column(String(255), nullable=False)
    VisitorBatter6Position = Column(Integer, nullable=False, default=0)
    VisitorBatter7ID       = Column(String(8), nullable=False)
    VisitorBatter7Name     = Column(String(255), nullable=False)
    VisitorBatter7Position = Column(Integer, nullable=False, default=0)
    VisitorBatter8ID       = Column(String(8), nullable=False)
    VisitorBatter8Name     = Column(String(255), nullable=False)
    VisitorBatter8Position = Column(Integer, nullable=False, default=0)
    VisitorBatter9ID       = Column(String(8), nullable=False)
    VisitorBatter9Name     = Column(String(255), nullable=False)
    VisitorBatter9Position = Column(Integer, nullable=False, default=0)
    
    HomeBatter1ID       = Column(String(8), nullable=False)
    HomeBatter1Name     = Column(String(255), nullable=False)
    HomeBatter1Position = Column(Integer, nullable=False, default=0)
    HomeBatter2ID       = Column(String(8), nullable=False)
    HomeBatter2Name     = Column(String(255), nullable=False)
    HomeBatter2Position = Column(Integer, nullable=False, default=0)
    HomeBatter3ID       = Column(String(8), nullable=False)
    HomeBatter3Name     = Column(String(255), nullable=False)
    HomeBatter3Position = Column(Integer, nullable=False, default=0)
    HomeBatter4ID       = Column(String(8), nullable=False)
    HomeBatter4Name     = Column(String(255), nullable=False)
    HomeBatter4Position = Column(Integer, nullable=False, default=0)
    HomeBatter5ID       = Column(String(8), nullable=False)
    HomeBatter5Name     = Column(String(255), nullable=False)
    HomeBatter5Position = Column(Integer, nullable=False, default=0)
    HomeBatter6ID       = Column(String(8), nullable=False)
    HomeBatter6Name     = Column(String(255), nullable=False)
    HomeBatter6Position = Column(Integer, nullable=False, default=0)
    HomeBatter7ID       = Column(String(8), nullable=False)
    HomeBatter7Name     = Column(String(255), nullable=False)
    HomeBatter7Position = Column(Integer, nullable=False, default=0)
    HomeBatter8ID       = Column(String(8), nullable=False)
    HomeBatter8Name     = Column(String(255), nullable=False)
    HomeBatter8Position = Column(Integer, nullable=False, default=0)
    HomeBatter9ID       = Column(String(8), nullable=False)
    HomeBatter9Name     = Column(String(255), nullable=False)
    HomeBatter9Position = Column(Integer, nullable=False, default=0)
    
    AdditionalInfo  = Column(String(255), nullable=False)
    AcquisitionInfo = Column(String(1), nullable=False)


    def setattr(self, attr, val):

        attr_type = str(getattr(Game, attr).property.columns[0].type)
        val_fmt = hlp.format_val(val, attr_type)
        
        setattr(self, attr, val_fmt)


    def __repr__(self):
       return "<Game(home='%s', away='%s')>" % (
                self.HomeTeam, self.VisitingTeam)


game_columns = [
    "Date",
    "DoubleHeader", "DayOfWeek",
    "VisitingTeam", "VisitingTeamLeague", "VisitingTeamGameNumber", "HomeTeam", "HomeTeamLeague", "HomeTeamGameNumber",
    "VisitorRunsScored", "HomeRunsScored",
    "LengthInOuts",
    "DayNight",
    "CompletionInfo", "ForfeitInfo", "ProtestInfo",
    "ParkID", "Attendance",
    "Duration",
    "VisitorLineScore", "HomeLineScore",
    "VisitorAB", "VisitorH", "Visitor2B", "Visitor3B", "VisitorHR", "VisitorRBI", "VisitorSH", "VisitorSF", "VisitorHBP", "VisitorBB", "VisitorIBB", "VisitorK", "VisitorSB", "VisitorCS", "VisitorGIDP", "VisitorCI", "VisitorLOB", "VisitorPitchers", "VisitorER", "VisitorTER", "VisitorWP", "VisitorBalks", "VisitorPO", "VisitorA", "VisitorE", "VisitorPB", "VisitorDP", "VisitorTP",
    "HomeAB", "HomeH", "Home2B", "Home3B", "HomeHR", "HomeRBI", "HomeSH", "HomeSF", "HomeHBP", "HomeBB", "HomeIBB", "HomeK", "HomeSB", "HomeCS", "HomeGIDP", "HomeCI", "HomeLOB", "HomePitchers", "HomeER", "HomeTER", "HomeWP", "HomeBalks", "HomePO", "HomeA", "HomeE", "HomePB", "HomeDP", "HomeTP",
    "UmpireHID", "UmpireHName", "Umpire1BID", "Umpire1BName", "Umpire2BID", "Umpire2BName", "Umpire3BID", "Umpire3BName", "UmpireLFID", "UmpireLFName", "UmpireRFID", "UmpireRFName",
    "VisitorManagerID", "VisitorManagerName", "HomeManagerID", "HomeManagerName",
    "VisitorStartingPitcherID", "VisitorStartingPitcherName", "HomeStartingPitcherID", "HomeStartingPitcherName",
    "WinningPitcherID", "WinningPitcherName", "LosingPitcherID", "LosingPitcherName", "SavingPitcherID", "SavingPitcherName",
    "GameWinningRBIID", "GameWinningRBIName",
    "VisitorBatter1ID", "VisitorBatter1Name", "VisitorBatter1Position", "VisitorBatter2ID", "VisitorBatter2Name", "VisitorBatter2Position", "VisitorBatter3ID", "VisitorBatter3Name", "VisitorBatter3Position", "VisitorBatter4ID", "VisitorBatter4Name", "VisitorBatter4Position", "VisitorBatter5ID", "VisitorBatter5Name", "VisitorBatter5Position", "VisitorBatter6ID", "VisitorBatter6Name", "VisitorBatter6Position", "VisitorBatter7ID", "VisitorBatter7Name", "VisitorBatter7Position", "VisitorBatter8ID", "VisitorBatter8Name", "VisitorBatter8Position", "VisitorBatter9ID", "VisitorBatter9Name", "VisitorBatter9Position",
    "HomeBatter1ID", "HomeBatter1Name", "HomeBatter1Position", "HomeBatter2ID", "HomeBatter2Name", "HomeBatter2Position", "HomeBatter3ID", "HomeBatter3Name", "HomeBatter3Position", "HomeBatter4ID", "HomeBatter4Name", "HomeBatter4Position", "HomeBatter5ID", "HomeBatter5Name", "HomeBatter5Position", "HomeBatter6ID", "HomeBatter6Name", "HomeBatter6Position", "HomeBatter7ID", "HomeBatter7Name", "HomeBatter7Position", "HomeBatter8ID", "HomeBatter8Name", "HomeBatter8Position", "HomeBatter9ID", "HomeBatter9Name", "HomeBatter9Position",
    "AdditionalInfo", "AcquisitionInfo"
]

