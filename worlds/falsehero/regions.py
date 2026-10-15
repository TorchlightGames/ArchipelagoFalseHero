from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import FalseHeroWorld


def create_and_connect_regions(world: FalseHeroWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: FalseHeroWorld) -> None:
    mountaintops_of_wisdom = Region("Mountaintops of Wisdom", world.player, world.multiworld)
    edge_of_the_mountaintops = Region("Edge of the Mountaintops", world.player, world.multiworld)
    prison_of_death = Region("Prison of Death", world.player, world.multiworld)
    land_of_birth_pre_vines = Region("Land of Birth (preVines)", world.player, world.multiworld)
    land_of_birth_post_vines = Region("Land of Birth (postVines)", world.player, world.multiworld)
    land_of_hope_starting_tower = Region("Land of Hope (startingTower)", world.player, world.multiworld)
    land_of_hope_village = Region("Land of Hope (village)", world.player, world.multiworld)
    sacrifice_pit = Region("Sacrifice pit", world.player, world.multiworld)
    temple_of_hope_pre_wings = Region("Temple of Hope (preWings)", world.player, world.multiworld)
    temple_of_hope_post_wings = Region("Temple of Hope (postWings)", world.player, world.multiworld)
    temple_of_hope_hidden_village = Region("Temple of Hope (hiddenVillage)", world.player, world.multiworld)
    dunes_of_passion_pre_flame = Region("Dunes of Passion (preFlame)", world.player, world.multiworld)
    dunes_of_passion_with_wings = Region("Dunes of Passion (withWings)", world.player, world.multiworld)
    dunes_of_passion_jail_cells = Region("Dunes of Passion (jail cells)", world.player, world.multiworld)
    dunes_of_passion_post_flame = Region("Dunes of Passion (postFlame)", world.player, world.multiworld)
    dunes_of_passion_post_essence = Region("Dunes of Passion (post essence)", world.player, world.multiworld)
    root_of_death = Region("Root of Death", world.player, world.multiworld)

    regions = [
        mountaintops_of_wisdom,
        edge_of_the_mountaintops,
        prison_of_death,
        land_of_birth_pre_vines,
        land_of_birth_post_vines,
        land_of_hope_starting_tower,
        land_of_hope_village,
        sacrifice_pit,
        temple_of_hope_pre_wings,
        temple_of_hope_post_wings,
        temple_of_hope_hidden_village,
        dunes_of_passion_pre_flame,
        dunes_of_passion_with_wings,
        dunes_of_passion_jail_cells,
        dunes_of_passion_post_flame,
        dunes_of_passion_post_essence,
        root_of_death
    ]

    world.multiworld.regions += regions


def connect_regions(world: FalseHeroWorld) -> None:
    mountaintops_of_wisdom = world.get_region("Mountaintops of Wisdom")
    edge_of_the_mountaintops = world.get_region("Edge of the Mountaintops")
    prison_of_death = world.get_region("Prison of Death")
    land_of_birth_pre_vines = world.get_region("Land of Birth (preVines)")
    land_of_birth_post_vines = world.get_region("Land of Birth (postVines)")
    land_of_hope_starting_tower = world.get_region("Land of Hope (startingTower)")
    land_of_hope_village = world.get_region("Land of Hope (village)")
    sacrifice_pit = world.get_region("Sacrifice pit")
    temple_of_hope_pre_wings = world.get_region("Temple of Hope (preWings)")
    temple_of_hope_post_wings = world.get_region("Temple of Hope (postWings)")
    temple_of_hope_hidden_village = world.get_region("Temple of Hope (hiddenVillage)")
    dunes_of_passion_pre_flame = world.get_region("Dunes of Passion (preFlame)")
    dunes_of_passion_with_wings = world.get_region("Dunes of Passion (withWings)")
    dunes_of_passion_jail_cells = world.get_region("Dunes of Passion (jail cells)")
    dunes_of_passion_post_flame = world.get_region("Dunes of Passion (postFlame)")
    dunes_of_passion_post_essence = world.get_region("Dunes of Passion (post essence)")
    root_of_death = world.get_region("Root of Death")

    mountaintops_of_wisdom.connect(edge_of_the_mountaintops, "MTW_EMT")

    edge_of_the_mountaintops.connect(prison_of_death, "EMT_PD")

    prison_of_death.connect(land_of_birth_pre_vines, "PD_LBpre")
    prison_of_death.connect(root_of_death, "PD_RD")

    land_of_birth_pre_vines.connect(land_of_birth_post_vines, "LBpre_LBpost")
    land_of_birth_pre_vines.connect(land_of_hope_starting_tower, "LBpre_LHtower")

    land_of_hope_starting_tower.connect(land_of_hope_village, "LHtower_LHvillage")

    land_of_hope_village.connect(temple_of_hope_pre_wings, "LHvillage_THpre")
    land_of_hope_village.connect(sacrifice_pit, "LHvillage_SP")

    temple_of_hope_pre_wings.connect(temple_of_hope_post_wings, "THpre_THpost")
    temple_of_hope_pre_wings.connect(temple_of_hope_hidden_village, "THpre_THvillage")
    temple_of_hope_pre_wings.connect(dunes_of_passion_pre_flame, "THpre_DPpre")

    dunes_of_passion_pre_flame.connect(dunes_of_passion_post_flame, "DPpre_DPpost")
    dunes_of_passion_pre_flame.connect(dunes_of_passion_with_wings, "DPpre_DPwings")
    dunes_of_passion_pre_flame.connect(dunes_of_passion_jail_cells, "DPpre_DPjail")

    dunes_of_passion_post_flame.connect(dunes_of_passion_post_essence, "DPpost_DPessence")

