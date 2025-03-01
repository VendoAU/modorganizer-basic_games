# Mod Organizer 2 - Simple Games Plugin

Mod Organizer 2 meta-plugin to make creating game plugins easier and faster.

## Why?

In order to create a MO2 game plugin, one must implement the `IPluginGame` interface.
This interface was initially designed for Bethesda games such as the Elder Scrolls or
Fallout series and thus contains a lot of things that are irrelevant for most games.

The goal of this meta-plugin is to allow creating game plugins for "basic" games by
providing a very simple python class.

## How to install?

Download the archive for your MO2 version and extract it directly into your MO2 `plugins` folder.

- Mod Organizer **2.3.2**: [Download](https://github.com/ModOrganizer2/modorganizer-basic_games/releases/download/v0.0.3/basic_games-0.0.3.zip)
  and extract in your `plugins/` folder (see below).
- Mod Organizer **2.4**: Basic games is included in Mod Organizer 2.4.
  - If you want to use new game plugins that have not been included in the
    release, [download the latest archive](https://github.com/ModOrganizer2/modorganizer-basic_games/archive/master.zip) and extract the files
    in the existing `basic_games` folder, overwriting existing files.

**Important:** Extract the *folder* in your `plugins` folder, not the individual files. Your
`plugins` folder should look like this:

```
dlls/
plugins/
  data/
  basic_games/
    games/
      __init__.py
      ...
    __init__.py
    basic_game.py
    ...
  bsa_extractor.dll
  ...
ModOrganizer.exe
```

You can rename `modorganizer-basic_games-xxx` to whatever you want (e.g., `basic_games`).

## Supported games

| Game | Author | File | Extras |
|------|--------|------|--------|
| The Binding of Isaac: Rebirth — [STEAM](https://store.steampowered.com/app/250900/The_Binding_of_Isaac_Rebirth/) |[EzioTheDeadPoet](https://github.com/EzioTheDeadPoet)|[game_thebindingofisaacrebirth.py](games/game_thebindingofisaacrebirth.py)|<ul><li>profile specific ini file</li></ul>|
| Darkest Dungeon — [GOG](https://www.gog.com/game/darkest_dungeon) / [STEAM](https://store.steampowered.com/app/262060/Darkest_Dungeon/) | [erri120](https://github.com/erri120) | [game_darkestdungeon.py](games/game_darkestdungeon.py) | <ul><li>save slot parsing</li><li>mod data checker</li></ul> |
| Dark Messiah of Might & Magic — [STEAM](https://store.steampowered.com/app/2100/Dark_Messiah_of_Might__Magic/) | [Holt59](https://github.com/holt59/) | [game_darkmessiahofmightandmagic.py](games/game_darkmessiahofmightandmagic.py) | <ul><li>save game preview</li></ul> |
| Dark Souls — [STEAM](https://store.steampowered.com/app/211420/DARK_SOULS_Prepare_To_Die_Edition/) | [Holt59](https://github.com/holt59/) | [game_darksouls.py](games/game_darkestdungeon.py) |  |
| Divinity: Original Sin (Classic) — [STEAM](https://store.steampowered.com/app/230230/Divinity_Original_Sin_Classic/) | [LostDragonist](https://github.com/LostDragonist/) | [game_divinityoriginalsin.py](games/game_divinityoriginalsin.py) | <ul><li>save game preview</li></ul> |
| Divinity: Original Sin (Enhanced Edition) — [STEAM](https://store.steampowered.com/app/373420/Divinity_Original_Sin__Enhanced_Edition/) | [LostDragonist](https://github.com/LostDragonist/) | [game_divinityoriginalsinee.py](games/game_divinityoriginalsinee.py) | <ul><li>save game preview</li><li>mod data checker</li></ul> |
| Dragon's Dogma: Dark Arisen — [GOG](https://www.gog.com/game/dragons_dogma_dark_arisen) / [STEAM](https://store.steampowered.com/app/367500/Dragons_Dogma_Dark_Arisen/) | [EzioTheDeadPoet](https://github.com/EzioTheDeadPoet) | [game_dragonsdogmadarkarisen.py](games/game_dragonsdogmadarkarisen.py) | |
| Dungeon Siege II — [GOG](https://www.gog.com/game/dungeon_siege_collection) / [STEAM](https://store.steampowered.com/app/39200/Dungeon_Siege_II/) | [Holt59](https://github.com/holt59/) | [game_dungeonsiege2.py](games/game_dungeonsiege2.py) | <ul><li>mod data checker</li></ul> |
| Kingdom Come: Deliverance — [GOG](https://www.gog.com/game/kingdom_come_deliverance) / [STEAM](https://store.steampowered.com/app/379430/Kingdom_Come_Deliverance/)| [Silencer711](https://github.com/Silencer711) | [game_kingdomcomedeliverance.py](games/game_kingdomcomedeliverance.py) | <ul><li>profile specific cfg files</li></ul>|
| Mirror's Edge — [GOG](https://www.gog.com/game/mirrors_edge) / [STEAM](https://store.steampowered.com/app/17410/Mirrors_Edge)|[EzioTheDeadPoet](https://eziothedeadpoet.github.io/AboutMe/)|[game_mirrorsedge.py](games/game_mirrorsedge.py)| |
| Mount & Blade II: Bannerlord — [GOG](https://www.gog.com/game/mount_blade_ii_bannerlord) / [STEAM](https://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/) | [Holt59](https://github.com/holt59/) | [game_mountandblade2.py](games/game_mountandblade2.py) | <ul><li>mod data checker</li></ul> |
| No Man's Sky - [GOG](https://www.gog.com/game/no_mans_sky) / [Steam](https://store.steampowered.com/app/275850/No_Mans_Sky/)|[EzioTheDeadPoet](https://eziothedeadpoet.github.io/AboutMe/)|[game_nomanssky.py](games/game_nomanssky.py)| |
| S.T.A.L.K.E.R. Anomaly — [MOD](https://www.stalker-anomaly.com/) | [Qudix](https://github.com/Qudix) | [game_stalkeranomaly.py](games/game_stalkeranomaly.py) | <ul><li>mod data checker</li></ul> |
| Stardew Valley — [GOG](https://www.gog.com/game/stardew_valley) / [STEAM](https://store.steampowered.com/app/413150/Stardew_Valley/) | [Syer10](https://github.com/Syer10), [Holt59](https://github.com/holt59/) | [game_stardewvalley.py](games/game_stardewvalley.py) | <ul><li>mod data checker</li></ul> |
| STAR WARS™ Empire at War: Gold Pack - [GOG](https://www.gog.com/game/star_wars_empire_at_war_gold_pack) / [STEAM](https://store.steampowered.com/app/32470/) | [erri120](https://github.com/erri120) | <ul><li>Empire at War: [game_starwars-empire-at-war.py](games/game_starwars-empire-at-war.py)</li><li>Force of Corruption: [game_starwars-empire-at-war-foc.py](games/game_starwars-empire-at-war-foc.py)</li></ul> | |
| Valheim — [STEAM](https://store.steampowered.com/app/892970/Valheim/) | [Zash](https://github.com/ZashIn) | [game_valheim.py](games/game_valheim.py) | <ul><li>mod data checker</li><li>overwrite config sync</li><li>save game support (no preview)</li></ul>
| The Witcher: Enhanced Edition - [GOG](https://www.gog.com/game/the_witcher) / [STEAM](https://store.steampowered.com/app/20900/The_Witcher_Enhanced_Edition_Directors_Cut/) | [erri120](https://github.com/erri120) | [game_witcher1.py](games/game_witcher1.py) | <ul><li>save game parsing (no preview)</li></ul> |
| The Witcher 3: Wild Hunt — [GOG](https://www.gog.com/game/the_witcher_3_wild_hunt) / [STEAM](https://store.steampowered.com/app/292030/The_Witcher_3_Wild_Hunt/) | [Holt59](https://github.com/holt59/) | [game_witcher3.py](games/game_witcher3.py) | <ul><li>save game preview</li></ul> |
| Yu-Gi-Oh! Master Duel — [STEAM](https://store.steampowered.com/app/1449850/) | [The Conceptionist](https://github.com/the-conceptionist) & [uwx](https://github.com/uwx) | [game_masterduel.py](games/game_masterduel.py) | |
| Zeus and Poseidon — [GOG](https://www.gog.com/game/zeus_poseidon) / [STEAM](https://store.steampowered.com/app/566050/Zeus__Poseidon/) | [Holt59](https://github.com/holt59/) | [game_zeusandpoiseidon.py](games/game_zeusandpoiseidon.py) | <ul><li>mod data checker</li></ul> |

## How to add a new game?

You can create a plugin by providing a python class in the `games` folder.

**Note:** If your game plugin does not load properly, you should set the log level
to debug and look at the `mo_interface.log` file.

You need to create a class that inherits `BasicGame` and put it in a `game_XX.py` in `games`.
Below is an example for The Witcher 3 (see also [games/game_witcher3.py](games/game_witcher3.py)):

```python
from PyQt5.QtCore import QDir
from ..basic_game import BasicGame


class Witcher3Game(BasicGame):

    Name = "Witcher 3 Support Plugin"
    Author = "Holt59"
    Version = "1.0.0a"

    GameName = "The Witcher 3"
    GameShortName = "witcher3"
    GameBinary = "bin/x64/witcher3.exe"
    GameDataPath = "Mods"
    GameSaveExtension = "sav"
    GameSteamId = 292030

    def savesDirectory(self):
        return QDir(self.documentsDirectory().absoluteFilePath("gamesaves"))
```

`BasicGame` inherits `IPluginGame` so you can override methods if you need to.
Each attribute you provide corresponds to a method (e.g., `Version` corresponds
to the `version` method, see the table below). If you override the method, you do
not have to provide the attribute:

```python
from PyQt5.QtCore import QDir
from ..basic_game import BasicGame

import mobase


class Witcher3Game(BasicGame):

    Name = "Witcher 3 Support Plugin"
    Author = "Holt59"

    GameName = "The Witcher 3"
    GameShortName = "witcher3"
    GameBinary = "bin/x64/witcher3.exe"
    GameDataPath = "Mods"
    GameSaveExtension = "sav"
    GameSteamId = 292030

    def version(self):
        # Don't forget to import mobase!
        return mobase.VersionInfo(1, 0, 0, mobase.ReleaseType.final)

    def savesDirectory(self):
        return QDir(self.documentsDirectory().absoluteFilePath("gamesaves"))
```

### List of valid keys

| Name | Description | `IPluginGame` method | Python |
|------|-------------|----------------------|--------|
| Name | Name of the plugin | `name` | `str` |
| Author | Author of the plugin | `author` | `str` |
| Version | Version of the plugin | `version` | `str` or `mobase.VersionInfo` |
| Description| Description (Optional) | `description` | `str` |
| GameName | Name of the game, as displayed by MO2 | `gameName` | `str` |
| GameShortName | Short name of the game | `gameShortName` | `str` |
| GameNexusName| Nexus name of the game (Optional, default to `GameShortName`) | `gameNexusName` | `str` |
| GameValidShortNames | Other valid short names (Optional) | `validShortNames` | `List[str]` or comma-separated list of values |
| GameNexusId | Nexus ID of the game (Optional) | `nexusGameID` | `str` or `int` |
| GameBinary | Name of the game executable, relative to the game path | `binaryName` | `str` |
| GameLauncher | Name of the game launcher, relative to the game path  (Optional) | `getLauncherName` | `str` |
| GameDataPath | Name of the folder containing mods, relative to game folder| `dataDirectory` | |
| GameDocumentsDirectory | Documents directory (Optional) | `documentsDirectory` | `str` or `QDir` |
| GameSavesDirectory | Directory containing saves (Optional, default to `GameDocumentsDirectory`) | `savesDirectory` | `str` or `QDir` |
| GameSaveExtension | Save file extension (Optional) `savegameExtension` | `str` |
| GameSteamId | Steam ID of the game (Optional) | `steamAPPId` | `List[str]` or `str` or `int` |
| GameGogId | GOG ID of the game (Optional) | `gogAPPId` | `List[str]` or `str` or `int` |
| GameOriginManifestIds | Origin Manifest ID of the game (Optional) | `originManifestIds` | `List[str]` or `str` |
| GameOriginWatcherExecutables | Executables to watch for Origin DRM (Optional) | `originWatcherExecutables` | `List[str]` or `str` |

You can use the following variables for `str`:

- `%DOCUMENTS%` will be replaced by the standard *Documents* folder.
- `%GAME_PATH%` will be replaced by the path to the game folder.
- `%GAME_DOCUMENTS%` will be replaced by the value of `GameDocumentsDirectory`.

## Extra features

The meta-plugin provides some useful extra feature:

1. **Automatic Steam, GOG, and Origin game detection:** If you provide Steam, GOG, or Origin IDs for the game (via
  `GameSteamId`, `GameGogId`, or `GameOriginManifestIds`), the game will be listed in the list of available games when creating a new
  MO2 instance (if the game is installed via Steam or GOG).
2. **Basic save game preview:** If you use the Python version, and if you can easily obtain a picture (file)
  for any saves, you can provide basic save-game preview by using the `BasicGameSaveGameInfo`.
  See [games/game_witcher3.py](games/game_witcher3.py) for  more details.

Game IDs can be found here:

- For Steam on [Steam Database](https://steamdb.info/)
- For GOG on [GOG Database](https://www.gogdb.org/)
- For Origin from C:\ProgramData\Origin\LocalContent (.mfst files)
