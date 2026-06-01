import alchemy.grimoire.dark_spellbook


allowed = alchemy.grimoire.dark_spellbook.dark_spell_allowed_ingredients()


def validate_ingredients(ingredients: str) -> str:
    lst = []
    lst = ingredients.split(", ")
    for ing in lst:
        if ing not in allowed:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
