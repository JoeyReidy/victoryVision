import csv

class RawPlayerStat:
    __slots__ = ["__MATCH_NAME", "__MATCH_ID", "__GAMEMODE", "__HP_MAP", "__HP_KILLS", "__HP_DEATHS", "__HP_DAMAGE", "__HILLTIME",
                  "__SND_MAP", "__SND_KILLS", "__SND_DEATHS", "__SND_DAMAGE", "__SND_PLANTS", "__SND_PLANTS", "__SND_FIRSTBLOODS",
                  "__CTRL_MAP", "__CTRL_KILLS", "__CTRL_DEATHS", "__CTRL_DAMAGE"]

    # def __init__(self, MATCH_NAME: str, MATCH_ID: str, GAMEMODE: str, HP_MAP: str, HP_KILLS: int, HP_DEATHS: int, HP_DAMAGE: int, 
    #              HILLTIME: int, SND_MAP: str, SND_KILLS: int, SND_DEATHS: int, SND_DAMAGE: int, SND_PLANTS: int, SND_FIRSTBLOODS: int,
    #              CTRL_MAP: str, CTRL_KILLS: int, CTRL_DEATHS: int, CTRL_DAMAGE: int):
    def __init__(self):
      self.__MATCH_NAME = ""
      self.__MATCH_ID = ""
      self.__GAMEMODE = ""

      self.__HP_MAP = ""
      self.__HP_KILLS = 0
      self.__HP_DEATHS = 0
      self.__HP_DAMAGE = 0
      self.__HILLTIME = 0

      self.__SND_MAP = ""
      self.__SND_KILLS = 0
      self.__SND_DEATHS = 0
      self.__SND_DAMAGE = 0
      self.__SND_PLANTS = 0
      self.__SND_FIRSTBLOODS = 0

      self.__CTRL_MAP = ""
      self.__CTRL_KILLS = 0
      self.__CTRL_DEATHS = 0
      self.__CTRL_DAMAGE = 0

    def openfile(self, filename):
        with open(filename, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row.


            for i in reader:
                self.__MATCH_NAME = i[0]
                self.__MATCH_ID = i[1]
                self.__GAMEMODE = i[2]

                self.__HP_MAP = i[3]
                self.__HP_KILLS = i[4]
                self.__HP_DEATHS = i[5]
                self.__HP_DAMAGE = i[6]
                self.__HILLTIME = i[7]

                self.__SND_MAP = i[8]
                self.__SND_KILLS = i[9]
                self.__SND_DEATHS = i[10]
                self.__SND_DAMAGE = i[11]
                self.__SND_PLANTS = i[12]
                self.__SND_FIRSTBLOODS = i[13]

                self.__CTRL_MAP = i[14]
                self.__CTRL_KILLS = i[15]
                self.__CTRL_DEATHS = i[16]
                self.__CTRL_DAMAGE = i[17]
                break

    def MatchHeader(self):
       return "Match Name:" + self.__MATCH_NAME + "\nMatch ID:" + self.__MATCH_ID + "\nGamemode:" + self.__GAMEMODE
    def HardpointHeader(self):
       return "HP Map:" + self.__HP_MAP 



def main():
  filename = "PlayerTemplateData.csv"
  player = RawPlayerStat()
  player.openfile(filename)
  print(player.MatchHeader())

if __name__ == "__main__":
    main()

