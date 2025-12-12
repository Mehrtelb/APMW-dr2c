import typing
from dataclasses import make_dataclass

from Options import Option, DefaultOnToggle, Toggle, Choice, Range, OptionDict, NamedRange, DeathLink, PerGameCommonOptions

class DeathLinkBehaviour(Choice):




DR2COptions = make_dataclass("DR2COptions", [(name, option) for name, option in dr2c_options.items()], bases=(PerGameCommonOptions,))