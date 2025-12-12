from worlds.AutoWorld import World

import typing

# Unresolved references to files in Archipelago
from BaseClasses import Region, Location, MultiWorld, Item, LocationProgressType, Tutorial, ItemClassification, \
    CollectionState
from worlds.AutoWorld import World, LogicMixin, WebWorld

# I am not sure if this even necessary
awbl_locations = {
    "Apartment Rescue",
    "Gym Apartment",
    "Riled Up Apartment",
    "Swarmed Apartment",
    "Dead Arcade",
    "Swarmed Arcade",
    "Bank",
    "Beautiful Beach",
    "Bookstore",
    "Cabin Rescue",
    "Cabin with Car",
    "Prepper Cabin",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
}

madeup_progression = {
    # Allows actually beating a mode by letting you into Canada
    "Passport",
    "ModeUnlock1", "ModeUnlock2", "ModeUnlock3"
}
# Not sure how this is gonna work, just placing it here for now
#
# Vanilla placements of the following items have no impact on logic, thus we can avoid creating these items and
# locations entirely when the option to randomize them is disabled.
logicless_options = {
    "WeaponSanity", "CostSanity"
}

class DR2CWeb(WebWorld):
    rich_text_options:doc = True

    setup_en = Tutorial(
        "Mod Setup and Use Guide",
        "A guide to playing Death Road to Canada with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mehrtelb"]
    )

    tutorials = [setup_en]
    theme = "partyTime"
    game_info_languages = ["en"]

    options_presets = {
        "Default": {
            "progression_balancing": 50,
            "starting_special_characters": 0,
            "starting_class": "random",
            "weaponsanity": "off",
            "costsanity": "off",
        }
    }

    bug_report_page = https://github.com/Mehrtelb/APMW-dr2c/issues/new?assignees=&labels=bug%2C+needs+investigation&template=bug_report.md&title=

class dr2c(World):
    """Death Road to Canada is a Randomly Generated Road Trip Action-RPG. You have to manage a car full of jerks as they
    explore cities, find weird people, and face up to 500 zombies at once.
    Everything's randomized: locations, events, survivor personalities. There's a different story every time you play.

    Find special events, rare encounters, and unique recruits. Find a grunting super-bodybuilder. Try to tame half-wild 
    dogs. Survivors have different personalities and quirks that may help or hinder you. Create 
    characters to find in the game. Make yourself, friends, family, and more! Share these custom jerks with others.

    Fight or flee from increasingly gigantic hordes of slow, classic-style zombies.
    Be careful, death is permanent!
    Make tough choices in Interactive Fiction text events. Get different results based on the traits of people in your 
    group.
    Start in Florida and try survive the journey to Canada, the last zombie-free nation!
    """  # from http://www.deathroadtocanada.com/
    game: str = "Death Road to Canada"
    options_dataclass = DR2COptions
    options: DR2COptions
    #    settings:

    web = DR2CWeb()

    ranges: typing.Dict[str, typing.Tuple[int, int]]
    zombo_points: int
    zombo_points_count: int?