from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as falsehero_options

class FalseHeroWorld(World):
    """
    False Hero is a fast-paced soulslike adventure where you steal your enemies’ attacks and chain them into deadly combos.
    Explore the corrupted Land of the Gods and put your combat skills to the true test in challenging boss fights.
    """

    game = "FalseHero"

    web = web_world.FalseHeroWebWorld()

    options_dataclass = falsehero_options.FalseHeroOptions
    options: falsehero_options.FalseHeroOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Mountaintops of Wisdom"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.FalseHeroItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def generate_early(self) -> None:
        self.multiworld.early_items[self.player]["Auditorium key"] = 1
        if self.options.force_early_combat_art:
            combat_art_index = self.random.randint(0, 30)
            combat_art_count = self.options.required_insight.value
            if combat_art_index == 0:
                self.multiworld.early_items[self.player]["Insight (Scholar of Wisdom)"] = combat_art_count
            elif combat_art_index == 1:
                self.multiworld.early_items[self.player]["Insight (Knowledge Keeper)"] = combat_art_count
            elif combat_art_index == 2:
                self.multiworld.early_items[self.player]["Insight (Ignorance)"] = combat_art_count
            elif combat_art_index == 3:
                self.multiworld.early_items[self.player]["Insight (Foreign Defense Machine)"] = combat_art_count
            elif combat_art_index == 4:
                self.multiworld.early_items[self.player]["Insight (Advanced Protection Unit)"] = combat_art_count
            elif combat_art_index == 5:
                self.multiworld.early_items[self.player]["Insight (Living Hand)"] = combat_art_count
            elif combat_art_index == 6:
                self.multiworld.early_items[self.player]["Insight (Shroomhead)"] = combat_art_count
            elif combat_art_index == 7:
                self.multiworld.early_items[self.player]["Insight (Physician of Birth)"] = combat_art_count
            elif combat_art_index == 8:
                self.multiworld.early_items[self.player]["Insight (Plant Knight)"] = combat_art_count
            elif combat_art_index == 9:
                self.multiworld.early_items[self.player]["Insight (Decaying Ape)"] = combat_art_count
            elif combat_art_index == 10:
                self.multiworld.early_items[self.player]["Insight (Dissolving Remains)"] = combat_art_count
            elif combat_art_index == 11:
                self.multiworld.early_items[self.player]["Insight (Immortal Child)"] = combat_art_count
            elif combat_art_index == 12:
                self.multiworld.early_items[self.player]["Insight (Decay)"] = combat_art_count
            elif combat_art_index == 13:
                self.multiworld.early_items[self.player]["Insight (Villager of Hopes Kingdom)"] = combat_art_count
            elif combat_art_index == 14:
                self.multiworld.early_items[self.player]["Insight (Disposed Sacrifice)"] = combat_art_count
            elif combat_art_index == 15:
                self.multiworld.early_items[self.player]["Insight (Headless Angel)"] = combat_art_count
            elif combat_art_index == 16:
                self.multiworld.early_items[self.player]["Insight (Sacrificial Mound)"] = combat_art_count
            elif combat_art_index == 17:
                self.multiworld.early_items[self.player]["Insight (Guardian Angel)"] = combat_art_count
            elif combat_art_index == 18:
                self.multiworld.early_items[self.player]["Insight (Scholar of Hope)"] = combat_art_count
            elif combat_art_index == 19:
                self.multiworld.early_items[self.player]["Insight (True Angel)"] = combat_art_count
            elif combat_art_index == 20:
                self.multiworld.early_items[self.player]["Insight (Vaour)"] = combat_art_count
            elif combat_art_index == 21:
                self.multiworld.early_items[self.player]["Insight (Despair)"] = combat_art_count
            elif combat_art_index == 22:
                self.multiworld.early_items[self.player]["Insight (Soldier of Passion)"] = combat_art_count
            elif combat_art_index == 23:
                self.multiworld.early_items[self.player]["Insight (Shield Golem)"] = combat_art_count
            elif combat_art_index == 24:
                self.multiworld.early_items[self.player]["Insight (Annihilation Unit)"] = combat_art_count
            elif combat_art_index == 25:
                self.multiworld.early_items[self.player]["Insight (Apostle of Death)"] = combat_art_count
            elif combat_art_index == 26:
                self.multiworld.early_items[self.player]["Insight (Apathy)"] = combat_art_count
            elif combat_art_index == 27:
                self.multiworld.early_items[self.player]["Insight (Passion)"] = combat_art_count
            elif combat_art_index == 28:
                self.multiworld.early_items[self.player]["Insight (Deathborn)"] = combat_art_count
            elif combat_art_index == 29:
                self.multiworld.early_items[self.player]["Insight (Pumping Vine)"] = combat_art_count

    def pre_fill(self) -> None:
        state = self.multiworld.get_all_state(False)
        unreachable = [
            r.name for r in self.multiworld.get_regions(self.player)
            if not r.can_reach(state)
        ]
        print("Unreachable regions with ALL items:", unreachable)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal",
            "required_insight",
            "auto_equip"
        )
