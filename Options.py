import typing
from dataclasses import make_dataclass

from Options import Option, DefaultOnToggle, Toggle, Choice, Range, OptionDict, NamedRange, DeathLink, PerGameCommonOptions

class DeathLinkBehaviour(Choice):


cost_sanity_weights: typing.Dict[str, type(Option)] = {}
for term, cost in cost_terms.items():
    option_name = f"CostSanity{cost.option}Weight"
    display_name = f"Costsanity {cost.option} Weight"
    extra_data = {
        "__module__": __name__, "range_end": 1000,
        "__doc__": (
            f"The likelihood of Costsanity choosing a {cost.option} cost."
            " Chosen as a sum of all weights from other types."
        ),
        "default": cost.weight
    }
    if cost == 'GEO':
        extra_data["__doc__"] += " Geo costs will never be chosen for Grubfather, Seer, or Egg Shop."

    option = type(option_name, (Range,), extra_data)
    option.display_name = display_name
    globals()[option.__name__] = option
    cost_sanity_weights[option.__name__] = option

dr2c_options: typing.Dict[str, type(Option)] = {
# A bunch of unresolved references and stuff I don't know what to do with yet
    **dr2c_randomize_options,
    RandomizeElevatorPass.__name__: RandomizeElevatorPass,
    **dr2c_logic_options,
    **{
        option.__name__: option
        for option in (
            StartLocation, Goal, GrubHuntGoal, WhitePalace, ExtraPlatforms, AddUnshuffledLocations, StartingGeo,
            DeathLink, DeathLinkShade, DeathLinkBreaksFragileCharms,
            MinimumGeoPrice, MaximumGeoPrice,
            MinimumGrubPrice, MaximumGrubPrice,
            MinimumEssencePrice, MaximumEssencePrice,
            MinimumCharmPrice, MaximumCharmPrice,
            RandomCharmCosts, PlandoCharmCosts,
            MinimumEggPrice, MaximumEggPrice, EggShopSlots,
            SlyShopSlots, SlyKeyShopSlots, IseldaShopSlots,
            SalubraShopSlots, SalubraCharmShopSlots,
            LegEaterShopSlots, GrubfatherRewardSlots,
            SeerRewardSlots, ExtraShopSlots,
            SplitCrystalHeart, SplitMothwingCloak, SplitMantisClaw,
            CostSanity, CostSanityHybridChance
        )
    },
    **cost_sanity_weights
}

DR2COptions = make_dataclass("DR2COptions", [(name, option) for name, option in dr2c_options.items()], bases=(PerGameCommonOptions,))