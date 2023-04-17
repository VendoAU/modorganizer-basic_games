import mobase
from ..basic_game import BasicGame
from ..basic_features.basic_save_game_info import BasicGameSaveGame
from PyQt5.QtCore import QFileInfo

from pathlib import Path


class Jazz2Game(BasicGame):
    Name = "Jazz Jackrabbit 2 Support Plugin"
    Author = "VendoAU"
    Version = "1.0.0"

    GameName = "Jazz Jackrabbit 2"
    GameShortName = "jazz2"
    GameBinary = "Jazz2.exe"
    GameDataPath = "%GAME_PATH%"
    GameDocumentsDirectory = "%GAME_PATH%"
    GameSavesDirectory = "%GAME_PATH%"
    GameGogId = ["1917711239", "1351891846", "1597842603"]

    def executables(self):
        if Path(self.gameDirectory().absoluteFilePath("Jazz2_NonPlus.exe")).exists():
            return [
                mobase.ExecutableInfo("Jazz Jackrabbit 2 Plus",
                                      QFileInfo(self.gameDirectory().absoluteFilePath("Jazz2.exe"))),
                mobase.ExecutableInfo("Jazz Jackrabbit 2",
                                      QFileInfo(self.gameDirectory().absoluteFilePath("Jazz2_NonPlus.exe")))
            ]
        return [
            mobase.ExecutableInfo("Jazz Jackrabbit 2", QFileInfo(self.gameDirectory().absoluteFilePath("Jazz2.exe")))
        ]

    def listSaves(self, folder):
        return [
            Jazz2Save(path)
            for path in Path(folder.absolutePath()).glob("SAVEGAME.*")
        ]

    def iniFiles(self):
        if Path(self.gameDirectory().absoluteFilePath("plus.ini")).exists():
            return ["plus.ini"]
        return []


class Jazz2DataChecker(mobase.ModDataChecker):
    def dataLooksValid(self, filetree) -> mobase.ModDataChecker.CheckReturn:
        return mobase.ModDataChecker.VALID


class Jazz2Save(BasicGameSaveGame):
    def getName(self):
        file = open(self._filepath, "rb")
        filecontents = file.read()
        file.close()

        imagelength = int.from_bytes(filecontents[4:6], "little")
        name = filecontents[8 + imagelength:][:32].decode()

        return name
