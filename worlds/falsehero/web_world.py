from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups


class FalseHeroWebWorld(WebWorld):
    game = "FalseHero"
    theme = "stone"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up False Hero for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["TorchlightGames"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
