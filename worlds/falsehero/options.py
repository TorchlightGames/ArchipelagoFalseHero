from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle


class Goal(Choice):
    """
    The win condition.
    """

    display_name = "Goal"

    option_defeat_deathborn = 0
    option_defeat_all_bosses = 1

    default = option_defeat_deathborn

class ConsumableChance(Range):
    """
    Percentage chance that any given filler item is a consumable and not an upgrade material.
    """

    display_name = "Consumable chance"

    range_start = 0
    range_end = 100
    default = 11

class RequiredInsight(Range):
    """
    Amount of Insight that needs to found to learn each Combat Art
    """

    display_name = "Required Insight"

    range_start = 1
    range_end = 3
    default = 1

class ForceEarlyCombatArt(DefaultOnToggle):
    """
    Ensure at least one Combat Art can be found in sphere 1
    """

    display_name = "Force early Combat Art"

class AutoEquip(Toggle):
    """
    Automatically equip Combat Arts, Scrolls & Clothing when they are received
    """

    display_name = "Auto-equip"


@dataclass
class FalseHeroOptions(PerGameCommonOptions):
    consumable_chance: ConsumableChance
    required_insight: RequiredInsight
    force_early_combat_art: ForceEarlyCombatArt
    goal: Goal
    auto_equip: AutoEquip


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "General Options",
        [Goal],
    ),
    OptionGroup(
        "Generation Options",
        [RequiredInsight, ForceEarlyCombatArt, ConsumableChance],
    ),
    OptionGroup(
        "Additional Options",
        [AutoEquip],
    ),
]