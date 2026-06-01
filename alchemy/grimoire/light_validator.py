import alchemy.grimoire.light_spellbook


def validate_ingredients(ingredients: str) -> str:
    lst = []
    lst = ingredients.split(", ")
    for ing in lst:
        if ing not in (
            alchemy.grimoire.light_spellbook
            .light_spell_allowed_ingredients()
        ):
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
