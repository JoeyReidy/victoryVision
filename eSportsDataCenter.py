import csv

class RawPlayerStat:
    __slots__ = ["__MATCH_NAME", "__MATCH_ID", "__GAMEMODE", "__HP_MAP", "__HP_KILLS", "__HP_DEATHS", "__HP_DAMAGE", "__HILLTIME",
                  "__SND_MAP", "__SND_KILLS", "__SND_DEATHS", "__SND_DAMAGE", "__SND_PLANTS", "__SND_PLANTS", "__SND_FIRSTBLOODS",
                  "__CTRL_MAP", "__CTRL_KILLS", "__CTRL_DEATHS", "__CTRL_DAMAGE"]

    def __init__(self, MATCH_NAME: str, MATCH_ID: str, GAMEMODE: str, HP_MAP: str, HP_KILLS: int, HP_DEATHS: int, HP_DAMAGE: int, 
                 HILLTIME: int, SND_MAP: str, SND_KILLS: int, SND_DEATHS: int, SND_DAMAGE: int, SND_PLANTS: int, SND_FIRSTBLOODS: int,
                 CTRL_MAP: str, CTRL_KILLS: int, CTRL_DEATHS: int, CTRL_DAMAGE: int):
      self.__MATCH_NAME = MATCH_NAME #[0]
      self.__MATCH_ID = MATCH_ID #[1]
      self.__GAMEMODE = GAMEMODE #[2] 

      self.__HP_MAP = HP_MAP #[3]
      self.__HP_KILLS = HP_KILLS #[4]
      self.__HP_DEATHS = HP_DEATHS #[5]
      self.__HP_DAMAGE = HP_DAMAGE #[6]
      self.__HILLTIME = HILLTIME #[7]

      self.__SND_MAP = SND_MAP #[8]
      self.__SND_KILLS = SND_KILLS #[9]
      self.__SND_DEATHS = SND_DEATHS #[10]
      self.__SND_DAMAGE = SND_DAMAGE #[11]
      self.__SND_PLANTS = SND_PLANTS #[12]]
      self.__SND_FIRSTBLOODS = SND_FIRSTBLOODS #[13]

      self.__CTRL_MAP = CTRL_MAP #[14]
      self.__CTRL_KILLS = CTRL_KILLS #[15]
      self.__CTRL_DEATHS = CTRL_DEATHS #[16]
      self.__CTRL_DAMAGE = CTRL_DAMAGE #[17]

    def MatchHeader(self):
       MatchHeader = []
       MatchHeader.add(self.__MATCH_NAME, self.__MATCH_ID, self.__GAMEMODE)
       return MatchHeader
       





def openfile(filename, RawPlayerStat, player):
  with open(filename, "r") as csv_file:
    reader = csv.reader(csv_file)
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for i in csv_reader:
            if(i.__contains__(" X")):
                print(i)

def main():
  filename = "PlayerTemplateData.csv"
  
  openfile(filename)

if __name__ == "__main__":
    main()

