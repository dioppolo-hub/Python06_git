import alchemy.grimoire.light_spellbook


allowed = alchemy.grimoire.light_spellbook.light_spell_allowed_ingredients()


def validate_ingredients(ingredients: str) -> str:
    lst = []
    lst = ingredients.split(", ")
    for ing in lst:
        if ing not in allowed:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
