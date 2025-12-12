from BaseClasses import ItemClassification
from typing import TypedDict, Dict, Set

item_table = {}

class DR2CItemData(NamedTuple):
    advancement: bool
    id: int
    type: str



item_name_groups: Dict[str, Set[str]] = {
    'Progression': {'Passport', 'Unlock Short Trip to Heck Mode', 'Unlock Long Winding Road Mode', 'Unlock Deadlier Road Mode', 'Unlock Familiar EXTREME', 'Unlock Rare EXTREME', 'Unlock Marathon Mode', 'Unlock KEPA MODE', 'Unlock Four Jerks EXTREME', 'Unlock ENDLESS MODE', 'Unlock OPP MODE', 'Unlock Quick Death MODE', 'Unlock INFECTION MODE', 'Unlock SEVERE WEATHER MODE', 'Unlock RPG MODE', 'Unlock Four Jerks SCEPTER', 'Unlock MUTATION MODE', 'Unlock INFECTION MODE EXTREME' },
    'Misc': {'Zombo Point', 'LevelUp', }
}