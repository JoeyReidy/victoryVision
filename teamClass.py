import csv

class RawTeamMatchStat:
    __slots__ = ["__MATCH_NAME", "__MATCH_ID", "__GAMEMODE", "__MAP", "__HP_RIT_SCORE", "__HP_OPP_SCORE", "__SND_RIT_SCORE", 
                 "__SND_OPP__SCORE", "__CTRL_RIT_SCORE", "__CTRL_OPP_SCORE"]

    def __init__(self, MATCH_NAME: str, MATCH_ID: str, GAMEMODE: str, MAP: str, HP_RIT_SCORE: int, HP_OPP_SCORE: int,
                 SND_RIT_SCORE: int, SND_OPP_SCORE: int, CTRL_RIT_SCORE, CTRL_OPP_SCORE: int):
      self.__MATCH_NAME = MATCH_NAME #[0]
      self.__MATCH_ID = MATCH_ID #[1]
       
      self.__GAMEMODE = GAMEMODE #[2]
      self.__HP_MAP = MAP #[3]
      
      self.__HP_RIT_SCORE = HP_RIT_SCORE #[4]
      self.__HP_OPP_SCORE = HP_OPP_SCORE #[5]
      self.__SND_RIT_SCORE = SND_RIT_SCORE #[6]
      self.__SND_OPP__SCORE = SND_OPP_SCORE #[7]
      self.__CTRL_RIT_SCORE = CTRL_RIT_SCORE #[8]
      self.__CTRL_OPP_SCORE = CTRL_OPP_SCORE #[9]


class Team:
  __slots__ = ["__team_name", "__matches", "__wins", "__losses", "__hp_wins", "__hp_losses", "__snd_wins", "__snd_losses", "__ctrl_wins",
                 "__ctrl_losses"]

  def __init__(self, team_name: str):
     self.__team_name = team_name
     self.__matches = []
     self.__wins = 0
     self.__losses = 0
     self.__hp_wins = 0
     self.__hp_losses = 0
     self.__snd_wins = 0
     self.__snd_losses = 0
     self.__ctrl_wins = 0
     self.__ctrl_losses = 0

  def add_match(self, match: RawTeamMatchStat):
    self.__matches.append(match)