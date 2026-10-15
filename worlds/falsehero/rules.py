from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, HasAny

from .options import Goal

if TYPE_CHECKING:
    from .world import FalseHeroWorld

def set_all_rules(world: FalseHeroWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: FalseHeroWorld) -> None:
    mountaintops_to_edge = world.get_entrance("MTW_EMT")
    edge_to_prison = world.get_entrance("EMT_PD")
    prison_to_birth_pre = world.get_entrance("PD_LBpre")
    prison_to_root = world.get_entrance("PD_RD")
    birth_pre_to_birth_post = world.get_entrance("LBpre_LBpost")
    birth_pre_to_hope_tower = world.get_entrance("LBpre_LHtower")
    hope_tower_to_hope_village = world.get_entrance("LHtower_LHvillage")
    hope_village_to_hope_temple_pre = world.get_entrance("LHvillage_THpre")
    hope_village_to_sacrifice_pit = world.get_entrance("LHvillage_SP")
    hope_temple_pre_to_hope_temple_post = world.get_entrance("THpre_THpost")
    hope_temple_pre_to_hope_temple_village = world.get_entrance("THpre_THvillage")
    hope_temple_pre_to_passion_pre = world.get_entrance("THpre_DPpre")
    passion_pre_to_passion_post = world.get_entrance("DPpre_DPpost")
    passion_pre_to_passion_wings = world.get_entrance("DPpre_DPwings")
    passion_pre_to_passion_jail = world.get_entrance("DPpre_DPjail")
    passion_post_to_passion_essence = world.get_entrance("DPpost_DPessence")

    world.set_rule(mountaintops_to_edge, Has("Auditorium key"))
    world.set_rule(edge_to_prison, Has("Rusty gate key"))
    world.set_rule(prison_to_birth_pre, HasAny("Essence of Wisdom", "Vines of Birth"))
    world.set_rule(prison_to_root, HasAll("Essence of Wisdom", "Essence of Birth", "Essence of Hope", "Essence of Passion"))
    world.set_rule(birth_pre_to_birth_post, Has("Vines of Birth"))
    world.set_rule(birth_pre_to_hope_tower, Has("Essence of Birth"))
    world.set_rule(hope_tower_to_hope_village, Has("Bloody sewer key"))
    world.set_rule(hope_village_to_sacrifice_pit, Has("Sacrificial pit key"))
    world.set_rule(hope_village_to_hope_temple_pre, Has("Vines of Birth"))
    world.set_rule(hope_temple_pre_to_hope_temple_post, Has("Wings of Hope"))
    world.set_rule(hope_temple_pre_to_hope_temple_village, HasAll("Golden winged key", "Wings of Hope"))
    world.set_rule(hope_temple_pre_to_passion_pre, Has("Essence of Hope"))
    world.set_rule(passion_pre_to_passion_post, Has("Red Flame of Passion"))
    world.set_rule(passion_pre_to_passion_wings, Has("Wings of Hope"))
    world.set_rule(passion_pre_to_passion_jail, Has("Jail key"))
    world.set_rule(passion_post_to_passion_essence, Has("Essence of Passion"))


def set_all_location_rules(world: FalseHeroWorld) -> None:
    world.set_rule(world.get_location("PD: Flask shard - robot workshop"), Has("Vines of Birth"))
    world.set_rule(world.get_location("BT: Invigorating flesh - open true angel painting"), Has("Golden canvas"))
    world.set_rule(world.get_location("PD: Invigorating flesh - wings of hope"), Has("Wings of Hope"))
    world.set_rule(world.get_location("TH/BHT: Invigorating flesh - villager death"), Has("Fresh meat", count = 2))
    world.set_rule(world.get_location("RRF: Luxurious ink - red flame room"), HasAny("Wings of Hope", "Red Flame of Passion"))
    world.set_rule(world.get_location("EMT: Mask shard - mysterious skull"), Has("Red Flame of Passion"))
    world.set_rule(world.get_location("LS: Physicians light - physician crystallized blood reward"), Has("Crystallized Blood"))
    world.set_rule(world.get_location("TB: Leonoras flower - leonoras cell"), Has("Cell key"))
    world.set_rule(world.get_location("PD: Engineers faceguard - robot workshop"), Has("Vines of Birth"))
    world.set_rule(world.get_location("TH/BHT: Bird mask - villager death"), Has("Fresh meat", count = 2))
    world.set_rule(world.get_location("PD: Scribal veil - scribe all texts reward"), HasAll("Memoir of Wisdom (first half)", "Memoir of Wisdom (second half)", "Leonoras journal (first half)", "Leonoras journal (second half)", "Acolytes testimony (first half)", "Acolytes testimony (second half)", "Writings of the Mask Maker (first half)", "Writings of the Mask Maker (second half)"))
    world.set_rule(world.get_location("TB: Leonoras journal (second half) - leonoras cell"), Has("Cell key"))
    world.set_rule(world.get_location("BT: Painting of a true angel - open true angel painting"), Has("Golden canvas"))
    world.set_rule(world.get_location("TH: Painting of despair - open despair painting"), Has("Golden canvas"))
    world.set_rule(world.get_location("TH: Acolytes testimony (second half) - open despair painting"), Has("Golden canvas"))
    world.set_rule(world.get_location("HV: Painting of a mysterious skull - open mysterious skull painting"), Has("Golden canvas"))
    world.set_rule(world.get_location("EMT: Brain tissue - mysterious skull"), Has("Red Flame of Passion"))
    world.set_rule(world.get_location("PD: Scroll of Ignorance - scribe memoir of Wisdom reward"), HasAll("Memoir of Wisdom (first half)", "Memoir of Wisdom (second half)"))
    world.set_rule(world.get_location("BSM: Scroll of everbloom - plant knight reward"), Has("Flower seedling"))
    world.set_rule(world.get_location("PD: Scroll of parasites - scribe leonoras journal reward"), HasAll("Leonoras journal (first half)", "Leonoras journal (second half)"))
    world.set_rule(world.get_location("DV: Scroll of the flesh devourer - villager reward"), Has("Fresh meat"))
    world.set_rule(world.get_location("BHT: Scroll of the dragon - shrine of the dragon"), HasAll("Breastplate of the dragon", "Legwear of the dragon", "Headpiece of the dragon"))
    world.set_rule(world.get_location("PD: Scroll of fear - scribe acolytes testimony reward"), HasAll("Acolytes testimony (first half)", "Acolytes testimony (second half)"))
    world.set_rule(world.get_location("HV: Scroll of fragility - open mysterious skull painting"), Has("Golden canvas"))
    world.set_rule(world.get_location("PD: Scroll of the Mask Maker - scribe writings of the mask maker reward"), HasAll("Writings of the Mask Maker (first half)", "Writings of the Mask Maker (second half)"))
    world.set_rule(world.get_location("TBO: Scroll of immortality - kill immortal child reward"), HasAll("Physicians tunic", "Physicians pants", "Red Flame of Passion"))
    world.set_rule(world.get_location("BHT: Scroll of the Philosophers - give acolyte brain tissue"), HasAll("Painting of a mysterious skull", "Brain tissue"))
    world.set_rule(world.get_location("RRF: Red Flame of Passion"), HasAny("Wings of Hope", "Red Flame of Passion"))

    has_book_throw = Has("Insight (Scholar of Wisdom)", count = 3)
    has_flamethrower = Has("Insight (Advanced Protection Unit)")
    has_living_hands = Has("Insight (Living Hand)", count = 4)
    has_rock_throw = Has("Insight (Decaying Ape)")
    has_blood_orb = Has("Insight (Villager of Hopes Kingdom)", count = 9)
    has_corpse_barrage = Has("Insight (Sacrificial Mound)")
    has_hopes_light = Has("Insight (Guardian Angel)", count = 4)
    has_laser = Has("Insight (True Angel)")
    has_lightning = Has("Insight (Vaour)")
    has_gun = Has("Insight (Annihilation Unit)", count = 3)
    has_spout = Has("Insight (Apathy)")

    has_ranged_ability = has_book_throw | has_flamethrower | has_living_hands | has_rock_throw | has_blood_orb | has_corpse_barrage | has_hopes_light | has_lightning | has_gun | has_spout
    has_hope_ability = has_hopes_light | has_laser

    world.set_rule(world.get_location("TH: Scroll of Hopes light - demonstrate light of hope"), has_hope_ability)
    world.set_rule(world.get_location("BSM: Flower seedling - across distant breakable tree"), has_ranged_ability)

    has_all_crystals = Has("Crystallized Blood", count = 2)
    can_finish_physician_quest = has_all_crystals & HasAll("Cell key", "Leonoras flower")

    world.set_rule(world.get_location("TB: Conjugated Bloodstones - physician quest reward"), can_finish_physician_quest)


def set_completion_condition(world: FalseHeroWorld) -> None:
    if world.options.goal == Goal.option_defeat_all_bosses:
        world.set_completion_rule(HasAll("Ignorance", "Advanced Protection Unit", "Decaying Ape", "Immortal Child", "Decay", "Sacrificial Mound", "True Angel", "Vaour", "Despair", "Apostle of Death", "Apathy", "Passion", "Deathborn"))
    else:
        world.set_completion_rule(Has("Deathborn"))