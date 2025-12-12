import typing
from dataclasses import make_dataclass

from Options import (Option, DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, OptionDict, NamedRange,
                     DeathLink, PerGameCommonOptions)

class Goal(Choice):
    """
    Defines the goal to accomplish in order to finish the game.
    - Certain Modes: Specify one or multiple modes you need to beat to finish the game.
    - Canada: Make it to Canada in any mode.
    """
    display_name = "Goal"
    certain_modes = 0
    canada = 1
    default = 0


class Passport(Toggle):
    """
    Dude, where's my passport? Since Canada is the last beacon of civilization, you will need a passport, I can't
    let you cross the border otherwise mate, sorry aboot that.
    Creates a 'Passport' item that needs to be collected before being able to finish a run.
    !WARNING EXTREMELY STUPID SETTING, WILL LIKELY SOFTLOCK OR FAIL TO GENERATE FOR NOW!
    """
    display_name = "Passport"

# -------------------- Goal: Certain Modes
# Not sure if this a good way to do it, but it's less tedious than listing all of them
class ChooseMode(FreeText):
    """
    Choose which mode you need to beat to finish the game: 'Death Road Normal Mode', 'Familiar Characters Mode',
    'Rare Characters Mode', 'Short Trip to Heck Mode', 'Long Winding Road Mode', 'Four Jerks Mode',
    'Deadlier Road Mode', 'Familiar EXTREME', 'Rare EXTREME', 'Marathon Mode', 'KEPA MODE', 'Four Jerks EXTREME',
    'OPP MODE', 'Quick Death MODE', 'INFECTION MODE', 'SEVERE WEATHER MODE', 'RPG MODE', 'Four Jerks SCEPTER',
    'MUTATION MODE' and 'INFECTION MODE EXTREME'
    """
    display_name = "ChooseMode"
