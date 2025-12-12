from typing import Dict, Callable, TYPE_CHECKING
from BaseClasses import CollectionState, LocationProgressType
from .Options import Goal, PaintingChecksBalancing

class DR2CRules:
    player: int
    world: DR2CWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    self.region_rules = {
        "Short Trip to Heck Mode": self.has_unlocked_stthm,
        "Long Winding Road Mode": self.has_unlocked_lwrm,
        "Deadlier Road Mode": self.has_unlocked_drm,
        "Familiar EXTREME": self.has_unlocked_fe,
        "Rare EXTREME": self.has_unlocked_re,
        "Marathon Mode": self.has_unlocked_mam,
        "KEPA MODE": self.has_unlocked_kepa,
        "Four Jerks EXTREME": self.has_unlocked_fje,
        "OPP MODE": self.has_unlocked_opp,
        "Quick Death MODE": self.has_unlocked_qdm,
        "INFECTION MODE": self.has_unlocked_im,
        "SEVERE WEATHER MODE": self.has_unlocked_swm,
        "RPG MODE": self.has_unlocked_rpgm,
        "Four Jerks SCEPTER": self.has_unlocked_fjs,
        "MUTATION MODE": self.has_unlocked_mum,
        "INFECTION MODE EXTREME": self.has_unlocked_ime
    }

# Maybe add a function that changes unlocks that are not needed to filler?

    def has_unlocked_stthm(self, state: CollectionState) -> bool:
        return state.has("Unlock Short Trip to Heck Mode", self.player)

    def has_unlocked_lwrm(self, state: CollectionState) -> bool:
        return state.has("Unlock Long Winding Road Mode", self.player)

    def has_unlocked_drm(self, state: CollectionState) -> bool:
        return state.has("Unlock Deadlier Road Mode", self.player)

    def has_unlocked_fe(self, state: CollectionState) -> bool:
        return state.has("Unlock Familiar EXTREME", self.player)

    def has_unlocked_re(self, state: CollectionState) -> bool:
        return state.has("Unlock Rare EXTREME", self.player)

    def has_unlocked_mam(self, state: CollectionState) -> bool:
        return state.has("Unlock Marathon Mode", self.player)

    def has_unlocked_kepa(self, state: CollectionState) -> bool:
        return state.has("Unlock KEPA MODE", self.player)

    def has_unlocked_fje(self, state: CollectionState) -> bool:
        return state.has("Unlock Four Jerks EXTREME", self.player)

    def has_unlocked_opp(self, state: CollectionState) -> bool:
        return state.has("Unlock OPP MODE", self.player)

    def has_unlocked_qdm(self, state: CollectionState) -> bool:
        return state.has("Unlock Quick Death MODE", self.player)

    def has_unlocked_im(self, state: CollectionState) -> bool:
        return state.has("Unlock INFECTION MODE", self.player)

    def has_unlocked_swm(self, state: CollectionState) -> bool:
        return state.has("Unlock SEVERE WEATHER MODE", self.player)

    def has_unlocked_rpgm(self, state: CollectionState) -> bool:
        return state.has("Unlock RPG MODE", self.player)

    def has_unlocked_fjs(self, state: CollectionState) -> bool:
        return state.has("Unlock Four Jerks SCEPTER", self.player)

    def has_unlocked_mum(self, state: CollectionState) -> bool:
        return state.has("Unlock MUTATION MODE", self.player)

    def has_unlocked_ime(self, state: CollectionState) -> bool:
        return state.has("Unlock INFECTION MODE EXTREME", self.player)