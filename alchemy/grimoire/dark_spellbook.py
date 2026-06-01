import alchemy.grimoire.dark_validator


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    temp = alchemy.grimoire.dark_validator.validate_ingredients(ingredients)
    if "INVALID" in temp:
        return "Rejected, Invalid Ingredients"
    elif "VALID" in temp:
        return f"Spell recorded: {spell_name} ({temp})"
    return "ERROR"
