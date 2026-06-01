import alchemy.grimoire.light_validator


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    temp = alchemy.grimoire.light_validator.validate_ingredients(ingredients)
    if "INVALID" in temp:
        return "Rejected, Invalid Ingredients"
    elif "VALID" in temp:
        return f"Spell recorded: {spell_name} ({temp})"
    return "ERROR"
