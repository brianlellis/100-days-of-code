from enum import Enum
from dataclasses import dataclass, frozen # frozen makes instances immutable

# --- 0. Enums (Remain the same as they are data definitions) ---
class EnumDrinkBrand(Enum):
    COKE = 1
    PEPSI = 2
    SPRITE = 3
    FANTA = 4
    SPECIAL_BLEND = 5

class EnumDrinkSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XL = 4
    COLOSSAL = 5

# --- 1. Immutable Data Structures (replacing classes for state) ---

@frozen # Makes instances immutable
@dataclass(kw_only=True) # Forces keyword-only arguments for clarity
class Drink:
    brand: EnumDrinkBrand
    size: EnumDrinkSize

@frozen
@dataclass(kw_only=True)
class SpecialEditionDrink:
    brand: EnumDrinkBrand
    size: EnumDrinkSize
    premium_ingredient: str # Specific to special edition drinks

# --- 2. Pure Functions (replacing methods and validators) ---

# Validation Functions (pure, no side effects)
def is_valid_brand(brand: EnumDrinkBrand) -> bool:
    """Checks if a brand is generally valid."""
    return brand in EnumDrinkBrand

def is_valid_size(size: EnumDrinkSize) -> bool:
    """Checks if a size is generally valid."""
    return size in EnumDrinkSize

# Creation Functions (replacing constructors/factories, they return new immutable data)
def create_drink(brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> Drink:
    """
    Pure function to create a standard Drink.
    Raises ValueError if inputs are invalid.
    """
    if not is_valid_brand(brand):
        raise ValueError(f"Invalid drink brand: {brand}")
    if not is_valid_size(size):
        raise ValueError(f"Invalid drink size: {size}")
    return Drink(brand=brand, size=size)

def create_special_edition_drink(
    brand: EnumDrinkBrand,
    size: EnumDrinkSize,
    premium_ingredient: str
) -> SpecialEditionDrink:
    """
    Pure function to create a special edition drink.
    Enforces specific brands/sizes.
    """
    if not is_valid_brand(brand) or brand != EnumDrinkBrand.SPECIAL_BLEND:
        raise ValueError(f"Invalid special edition drink brand: {brand}")
    if not is_valid_size(size) or size != EnumDrinkSize.COLOSSAL:
        raise ValueError(f"Invalid special edition drink size: {size}. Must be COLOSSAL for special editions.")
    return SpecialEditionDrink(brand=brand, size=size, premium_ingredient=premium_ingredient)


# "Setter" Functions (they return NEW immutable objects)
def set_drink_brand(drink: Drink, new_brand: EnumDrinkBrand) -> Drink:
    """Returns a new Drink with the updated brand."""
    if not is_valid_brand(new_brand):
        raise ValueError(f"Invalid brand: {new_brand}")
    return Drink(brand=new_brand, size=drink.size)

def set_drink_size(drink: Drink, new_size: EnumDrinkSize) -> Drink:
    """Returns a new Drink with the updated size."""
    if not is_valid_size(new_size):
        raise ValueError(f"Invalid size: {new_size}")
    return Drink(brand=drink.brand, size=new_size)

# Description Functions (pure, operate on the data)
def get_drink_name(drink: Drink) -> str:
    return f"{drink.brand.name} Drink"

def describe_drink(drink: Drink) -> str:
    """Pure function to describe a general drink."""
    return f"{drink.size.name} {drink.brand.name} Drink"

def describe_special_edition_drink(drink: SpecialEditionDrink) -> str:
    """Pure function to describe a special edition drink."""
    return f"{drink.size.name} {drink.brand.name} Drink with {drink.premium_ingredient}"


# --- 3. Functional "Fluent API" (Function Composition) ---
# Instead of methods returning self, functions accept and return the data structure.

def fluent_drink_builder(initial_brand: EnumDrinkBrand, initial_size: EnumDrinkSize = EnumDrinkSize.MEDIUM):
    """
    Returns a builder function that allows chaining.
    This closure captures the current state of the drink being built.
    """
    current_drink = create_drink(initial_brand, initial_size)

    def builder_func(transform_func):
        nonlocal current_drink
        current_drink = transform_func(current_drink)
        return builder_func # Return self (the builder_func) for chaining

    def build_func():
        return current_drink

    # Attach the build_func to the builder_func for the final step
    builder_func.build = build_func
    return builder_func

# Helper for fluent API to apply brand change
def with_brand(new_brand: EnumDrinkBrand):
    def _inner(drink: Drink):
        return set_drink_brand(drink, new_brand)
    return _inner

# Helper for fluent API to apply size change
def with_size(new_size: EnumDrinkSize):
    def _inner(drink: Drink):
        return set_drink_size(drink, new_size)
    return _inner
    