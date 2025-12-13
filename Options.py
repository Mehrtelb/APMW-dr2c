import typing
from dataclasses import make_dataclass

from Options import (Option, DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, OptionDict, NamedRange,
                     DeathLink, PerGameCommonOptions)

class Goal(Choice):
    """
    Defines the goal to accomplish in order to finish the game.
    - Specific Modes: Specify one or multiple modes you need to beat to finish the game.
    - Random Modes: Specify how many randomly chosen modes you need to beat to finish the game.
    - Canada: Make it to Canada in any mode. Good if you want a very short game.
    """
    display_name = "Goal"
    specific_modes = 0
    random_modes = 1
    canada = 2
    default = 0

class GoalNumLevels(BaseOptions.Range):
    """
    If 'Specific Modes' or 'Random Modes' are chosen as the goal, this is how many Modes must be beaten.
    Each Mode takes about 45 minutes (Short Trip is shorter and Long Winding and Marathon are longer respectively
    but could take a lot longer with Death Link enabled) and adds 3-4 Locations.
    """
    display_name = "Goal: Number of Modes"
    range_start = 1
    range_end = 20
    default = 3

class GoalSpecificModes(BaseOptions.OptionSet):
    """
    If 'Specific Modes' is chosen as the goal, all modes chosen here must be beaten to finish the game.
    """
    display_name = "Goal: Specific Modes"
    valid_keys = frozenset({
        "Death Road Normal Mode",
        "Familiar Characters Mode",
        "Rare Characters Mode",
        "Short Trip to Heck Mode",
        "Long Winding Road Mode",
        "Four Jerks Mode",
        "Deadlier Road Mode",
        "Familiar EXTREME",
        "Rare EXTREME",
        "Marathon Mode",
        "KEPA MODE",
        "Four Jerks EXTREME",
        "OPP MODE",
        "Quick Death MODE",
        "INFECTION MODE",
        "SEVERE WEATHER MODE",
        "RPG MODE",
        "Four Jerks SCEPTER",
        "MUTATION MODE",
        "INFECTION MODE EXTREME",
    })
    default = frozenset({
        "Death Road Normal Mode",
        "Short Trip to Heck Mode",
        "Deadlier Road Mode",
    })

class ZomboPointsMultiplier(Range):
    """
    Multiplies the amount of Zombo Points you gain from Pickups and Events.
    Choosing 0 disables Zombo Points, why would you do that though?
    """
    display_name = "Zombo Points Multiplier"
    range_start = 0
    range_end = 100
    default = 10

class Passport(Toggle):
    """
    Dude, where's my passport? Since Canada is the last beacon of civilization, you will need a passport, I can't
    let you cross the border otherwise mate, sorry aboot that.
    Creates a 'Passport' item that needs to be collected before being able to finish a run.
    !WARNING EXTREMELY STUPID SETTING, WILL VERY LIKELY CAUSE YOU TO BK UNLESS YOU FORCE THIS TO BE A LOCAL ITEM!
    """
    display_name = "Passport"
