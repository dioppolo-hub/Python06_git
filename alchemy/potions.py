from alchemy.elements import create_earth
from alchemy import create_air
import elements


def healing_potion() -> str:
    return f"Healing Potion brewed with\
 '{create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
    return f"strength Potion brewed with\
 '{elements.create_fire()}' and '{elements.create_water()}'"
