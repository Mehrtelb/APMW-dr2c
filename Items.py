

item_table = {}

class DR2CItemData(NamedTuple):
    advancement: bool
    id: int
    type: str

for i, (item_name, item_type) in enumerate(items.items(), start=0x1000000):
    item_table[item_name] = DR2CItemData(advancement=item_name in logic_items or item_name in item_effects,
                                       id=i, type=item_type)