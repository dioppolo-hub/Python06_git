import alchemy.grimoire.light_spellbook


def validate_ingredients(ingredients: str) -> str:
    if ingredients in\
        alchemy.grimoire.light_spellbook.light_spell_allowed_ingredients():
            return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"