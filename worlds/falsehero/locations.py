from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple
import csv
import io
import pkgutil

from BaseClasses import Location, LocationProgressType

from . import items

if TYPE_CHECKING:
    from .world import FalseHeroWorld


class LocationData(NamedTuple):
    name: str
    id: int
    region: str
    missable: bool = False


def parse_bool(text: str | None) -> bool:
    return (text or "").strip().lower() == "true"

def read_location_table() -> list[LocationData]:
    raw = pkgutil.get_data(__package__, "tables/table_locations.csv")
    if raw is None:
        raise FileNotFoundError("tables/table_locations.csv not found in world package")

    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))

    return [
        LocationData(
            name = row["Name"].strip(),
            id = int(row["ID"]),
            region = row["Region"].strip(),
            missable = parse_bool(row["Missable"]),
        )
        for row in reader
        if row["ID"].strip()
    ]


LOCATION_TABLE: list[LocationData] = read_location_table()
LOCATION_NAME_TO_ID: dict[str, int] = {loc.name: loc.id for loc in LOCATION_TABLE}

LOCATIONS_BY_REGION: dict[str, list[LocationData]] = {}
for _loc in LOCATION_TABLE:
    LOCATIONS_BY_REGION.setdefault(_loc.region, []).append(_loc)

MISSABLE_LOCATION_NAMES: frozenset[str] = frozenset(
    loc.name for loc in LOCATION_TABLE if loc.missable
)


class FalseHeroLocation(Location):
    game = "FalseHero"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: FalseHeroWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: FalseHeroWorld) -> None:
    for region_name, locations in LOCATIONS_BY_REGION.items():
        region = world.get_region(region_name)
        region.add_locations(
            {loc.name: loc.id for loc in locations},
            FalseHeroLocation,
        )

        for location in region.locations:
            if location.name in MISSABLE_LOCATION_NAMES:
                location.progress_type = LocationProgressType.EXCLUDED


def create_events(world: FalseHeroWorld) -> None:
    edge_of_the_mountaintops = world.get_region("Edge of the Mountaintops")
    land_of_birth_pre = world.get_region("Land of Birth (preVines)")
    land_of_birth_post = world.get_region("Land of Birth (postVines)")
    sacrifice_pit = world.get_region("Sacrifice pit")
    hope_temple_pre = world.get_region("Temple of Hope (preWings)")
    hope_temple_post = world.get_region("Temple of Hope (postWings)")
    hope_temple_village = world.get_region("Temple of Hope (hiddenVillage)")
    passion_post = world.get_region("Dunes of Passion (postFlame)")
    root_of_death = world.get_region("Root of Death")

    edge_of_the_mountaintops.add_event(
        "Defeat Ignorance", "Ignorance", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    land_of_birth_pre.add_event(
        "Defeat Advanced Protection Unit", "Advanced Protection Unit", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    land_of_birth_pre.add_event(
        "Defeat Decaying Ape", "Decaying Ape", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    land_of_birth_pre.add_event(
        "Defeat Immortal Child", "Immortal Child", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    land_of_birth_post.add_event(
        "Defeat Decay", "Decay", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    sacrifice_pit.add_event(
        "Defeat Sacrificial Mound", "Sacrificial Mound", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    hope_temple_pre.add_event(
        "Defeat True Angel", "True Angel", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    hope_temple_post.add_event(
        "Defeat Vaour", "Vaour", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    hope_temple_village.add_event(
        "Defeat Despair", "Despair", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    passion_post.add_event(
        "Defeat Apostle of Death", "Apostle of Death", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    passion_post.add_event(
        "Defeat Apathy", "Apathy", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    passion_post.add_event(
        "Defeat Passion", "Passion", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
    root_of_death.add_event(
        "Defeat Deathborn", "Deathborn", location_type=FalseHeroLocation, item_type=items.FalseHeroItem
    )
