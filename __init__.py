from worlds.AutoWorld import World

import typing

from .Items import item_table, item_name_groups

# Unresolved references to files in Archipelago
from BaseClasses import Region, Location, MultiWorld, Item, LocationProgressType, Tutorial, ItemClassification, \
    CollectionState
from worlds.AutoWorld import World, LogicMixin, WebWorld



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
    rich_text_options_doc = True

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

    options_presets = options_presets

    bug_report_page = https://github.com/Mehrtelb/APMW-dr2c/issues/new?assignees=&labels=bug%2C+needs+investigation&template=bug_report.md&title=

class DR2CContainer(APPlayerContainer):
    game: str = "Death Road to Canada"

    def __init__(
            self,
            config_json: str,
            options_json: str,
            outfile_name: str,
            output_directory: str,
            player: Optional[int] = None,
            player_name: str = "",
            server: str = ""):
        self.config_json = config_json
        self.config_path = "config.json"
        self.options_path = "options.json"
        self.options_json = options_json
        container_path = os.path.join(output_directory, outfile_name + ".krtdl")
        super().__init__(container_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr(self.config_path, self.config_json)
        opened_zipfile.writestr(self.options_path, self.options_json)
        super().write_contents(opened_zipfile)

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
    topology_present = False
    settings: typing.ClassVar[DeathRoadtoCanadaSettings]

    web = DR2CWeb()

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    item_name_groups = Items.item_name_groups

    ranges: typing.Dict[str, typing.Tuple[int, int]]
    zombo_points: int
    zombo_points_count: int?

    # decent place to implement progressive items, in most cases can stay as-is
    def collect_item(self, state: "CollectionState", item: "Item", remove: bool = False) -> Optional[str]:
        """
        Collect an item name into state. For speed reasons items that aren't logically useful get skipped.
        Collect None to skip item.
        :param state: CollectionState to collect into
        :param item: Item to decide on if it should be collected into state
        :param remove: indicate if this is meant to remove from state instead of adding.
        """
        if item.advancement:
            return item.name
        return None

    def get_pre_fill_items(self) -> List["Item"]:
        """
        Used to return items that need to be collected when creating a fresh all_state, but don't exist in the
        multiworld itempool.
        """
        return []

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        """Called when an item is collected in to state. Useful for things such as progressive items or currency."""
        name = self.collect_item(state, item)
        if name:
            state.add_item(name, self.player)
            return True
        return False

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        """Called when an item is removed from to state. Useful for things such as progressive items or currency."""
        name = self.collect_item(state, item, True)
        if name:
            state.remove_item(name, self.player)
            return True
        return False

    # following methods should not need to be overridden.
    def create_filler(self) -> "Item":
        return self.create_item(self.get_filler_item_name())

    # convenience methods
    def get_location(self, location_name: str) -> "Location":
        return self.multiworld.get_location(location_name, self.player)

    def get_locations(self) -> "Iterable[Location]":
        return self.multiworld.get_locations(self.player)

    def get_entrance(self, entrance_name: str) -> "Entrance":
        return self.multiworld.get_entrance(entrance_name, self.player)

    def get_entrances(self) -> "Iterable[Entrance]":
        return self.multiworld.get_entrances(self.player)

    def get_region(self, region_name: str) -> "Region":
        return self.multiworld.get_region(region_name, self.player)

    def get_regions(self) -> "Iterable[Region]":
        return self.multiworld.get_regions(self.player)

    def push_precollected(self, item: Item) -> None:
        self.multiworld.push_precollected(item)

    @property
    def player_name(self) -> str:
        return self.multiworld.get_player_name(self.player)

    @classmethod
    def get_data_package_data(cls) -> "GamesPackage":
        sorted_item_name_groups = {
            name: sorted(cls.item_name_groups[name]) for name in sorted(cls.item_name_groups)
        }
        sorted_location_name_groups = {
            name: sorted(cls.location_name_groups[name]) for name in sorted(cls.location_name_groups)
        }
        res: "GamesPackage" = {
            # sorted alphabetically
            "item_name_groups": sorted_item_name_groups,
            "item_name_to_id": cls.item_name_to_id,
            "location_name_groups": sorted_location_name_groups,
            "location_name_to_id": cls.location_name_to_id,
        }
        res["checksum"] = data_package_checksum(res)
        return res


# any methods attached to this can be used as part of CollectionState,
# please use a prefix as all of them get clobbered together
class LogicMixin(metaclass=AutoLogicRegister):
    pass


def data_package_checksum(data: "GamesPackage") -> str:
    """Calculates the data package checksum for a game from a dict"""
    assert "checksum" not in data, "Checksum already in data"
    assert sorted(data) == list(data), "Data not ordered"
    from NetUtils import encode
    return hashlib.sha1(encode(data).encode()).hexdigest()