from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple
import pkgutil
import csv
import io

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import FalseHeroWorld


class ItemData(NamedTuple):
    name: str
    id: int
    classification: ItemClassification
    count: int = 1


def parse_classification(text: str) -> ItemClassification:
    result = ItemClassification(0)
    for part in text.split("|"):
        try:
            result |= ItemClassification[part.strip().lower()]
        except KeyError:
            raise ValueError(f"Unknown item classification {part!r} in table_items.csv") from None
    return result

def read_item_table() -> list[ItemData]:
    raw = pkgutil.get_data(__package__, "tables/table_items.csv")
    if raw is None:
        raise FileNotFoundError("tables/table_items.csv not found in world package")

    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))

    return [
        ItemData(
            name = row["Name"].strip(),
            id = int(row["ID"]),
            classification = parse_classification(row["Classification"]),
            count = int(row["Count"] or 1),
        )
        for row in reader
        if row["ID"].strip()
    ]


ITEM_TABLE: list[ItemData] = read_item_table()
ITEM_NAME_TO_ID: dict[str, int] = {item.name: item.id for item in ITEM_TABLE}
DEFAULT_ITEM_CLASSIFICATIONS: dict[str, ItemClassification] = {
    item.name: item.classification for item in ITEM_TABLE
}
ITEM_COUNTS: dict[str, int] = {item.name: item.count for item in ITEM_TABLE}


class FalseHeroItem(Item):
    game = "FalseHero"

def get_random_filler_item_name(world: FalseHeroWorld) -> str:
    if world.random.randint(0, 99) < world.options.consumable_chance:
        chance = 33
        rand_number = world.random.randint(0, 99)

        if rand_number < chance:
            return "Mask shard"
        elif rand_number < chance + chance:
            return "Invigorating flesh"
        else:
            return "Blood needle"
    else:
        scraps_of_ink_chance = 33
        scraps_of_ink_death_chance = 13
        dried_ink_chance = 25
        dried_ink_death_chance = 8
        common_ink_chance = 17
        common_ink_death_chance = 4
        rand_number = world.random.randint(0, 99)

        if rand_number < scraps_of_ink_chance:
            return "Scraps of ink"
        elif rand_number < scraps_of_ink_chance + scraps_of_ink_death_chance:
            return "Scraps of ink (Death infused)"
        elif rand_number < scraps_of_ink_chance + scraps_of_ink_death_chance + dried_ink_chance:
            return "Dried ink"
        elif rand_number < scraps_of_ink_chance + scraps_of_ink_death_chance + dried_ink_chance + dried_ink_death_chance:
            return "Dried ink (Death infused)"
        elif rand_number < scraps_of_ink_chance + scraps_of_ink_death_chance + dried_ink_chance + dried_ink_death_chance + common_ink_chance:
            return "Common ink"
        elif rand_number < scraps_of_ink_chance + scraps_of_ink_death_chance + dried_ink_chance + dried_ink_death_chance + common_ink_chance + common_ink_death_chance:
            return "Common ink (Death infused)"

    return "Scraps of ink"


def create_item_with_correct_classification(world: FalseHeroWorld, name: str) -> FalseHeroItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return FalseHeroItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: FalseHeroWorld) -> None:
    itempool: list[Item] = []
    for item in ITEM_TABLE:
        if item.id > 2000 and item.id < 3000:
            itempool.extend(world.create_item(item.name) for _ in range(world.options.required_insight))
        else:
            itempool.extend(world.create_item(item.name) for _ in range(item.count))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
