from abc import ABC, abstractmethod
from enum import Enum

# --- 0. Enums (Copied for self-containment) ---
class EnumDrinkBrand(Enum):
    COKE = 1
    PEPSI = 2
    SPRITE = 3
    FANTA = 4
    SPECIAL_BLEND = 5 # New brand for special edition drinks

class EnumDrinkSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XL = 4
    COLOSSAL = 5 # New size for special edition drinks

# --- Existing SOLID Abstractions and Implementations ---

class IDrinkValidator(ABC):
    @abstractmethod
    def is_valid_brand(self, brand: EnumDrinkBrand) -> bool:
        pass

    @abstractmethod
    def is_valid_size(self, size: EnumDrinkSize) -> bool:
        pass

class EnumDrinkValidator(IDrinkValidator):
    def is_valid_brand(self, brand: EnumDrinkBrand) -> bool:
        return brand in EnumDrinkBrand

    def is_valid_size(self, size: EnumDrinkSize) -> bool:
        return size in EnumDrinkSize

class IProduct(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass

class IDrink(IProduct, ABC):
    @abstractmethod
    def get_brand(self) -> EnumDrinkBrand:
        pass

    @abstractmethod
    def get_size(self) -> EnumDrinkSize:
        pass

    @abstractmethod
    def set_brand(self, brand: EnumDrinkBrand):
        pass

    @abstractmethod
    def set_size(self, size: EnumDrinkSize):
        pass

class SolidDrinks(IDrink):
    def __init__(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM,
                 validator: IDrinkValidator = None):
        self.__validator = validator if validator is not None else EnumDrinkValidator()

        if not self.__validator.is_valid_brand(brand):
            raise ValueError(f"Invalid drink brand: {brand}")
        self.__brand = brand

        if not self.__validator.is_valid_size(size):
            raise ValueError(f"Invalid drink size: {size}")
        self.__size = size

    def set_brand(self, brand: EnumDrinkBrand):
        if not self.__validator.is_valid_brand(brand):
            raise ValueError(f"Invalid drink brand: {brand}")
        self.__brand = brand

    def get_brand(self) -> EnumDrinkBrand:
        return self.__brand

    def set_size(self, size: EnumDrinkSize):
        if not self.__validator.is_valid_size(size):
            raise ValueError(f"Invalid drink size: {size}")
        self.__size = size

    def get_size(self) -> EnumDrinkSize:
        return self.__size

    def get_name(self) -> str:
        return f"{self.__brand.name} Drink"

    def describe(self) -> str:
        return f"{self.__size.name} {self.__brand.name} Drink"

class IDrinkFactory(ABC):
    @abstractmethod
    def create_drink(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> IDrink:
        pass

class SolidDrinkFactory(IDrinkFactory):
    def __init__(self, validator: IDrinkValidator = None):
        self.__validator = validator if validator is not None else EnumDrinkValidator()

    def create_drink(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> IDrink:
        return SolidDrinks(brand, size, validator=self.__validator)

# --- NEW: A different type of Drink and its corresponding Factory ---

class SpecialEditionSolidDrinks(IDrink):
    """
    A special edition drink class, implementing IDrink, with unique characteristics.
    """
    def __init__(self, brand: EnumDrinkBrand, size: EnumDrinkSize, premium_ingredient: str,
                 validator: IDrinkValidator = None):
        self.__validator = validator if validator is not None else EnumDrinkValidator()

        if not self.__validator.is_valid_brand(brand) or brand not in [EnumDrinkBrand.SPECIAL_BLEND]:
            raise ValueError(f"Invalid special edition drink brand: {brand}")
        self.__brand = brand

        if not self.__validator.is_valid_size(size) or size not in [EnumDrinkSize.COLOSSAL]:
            raise ValueError(f"Invalid special edition drink size: {size}")
        self.__size = size
        self.__premium_ingredient = premium_ingredient

    def set_brand(self, brand: EnumDrinkBrand):
        if not self.__validator.is_valid_brand(brand):
            raise ValueError(f"Invalid drink brand: {brand}")
        self.__brand = brand

    def get_brand(self) -> EnumDrinkBrand:
        return self.__brand

    def set_size(self, size: EnumDrinkSize):
        if not self.__validator.is_valid_size(size):
            raise ValueError(f"Invalid drink size: {size}")
        self.__size = size

    def get_size(self) -> EnumDrinkSize:
        return self.__size

    def get_name(self) -> str:
        return f"Special Edition {self.__brand.name} Drink"

    def describe(self) -> str:
        return f"{self.__size.name} {self.__brand.name} Drink with {self.__premium_ingredient}"

class SpecialEditionDrinkFactory(IDrinkFactory):
    """
    A concrete factory for creating SpecialEditionSolidDrinks.
    It implements the same IDrinkFactory interface as SolidDrinkFactory.
    """
    def __init__(self, default_ingredient: str = "Unicorn Dust", validator: IDrinkValidator = None):
        self.__default_ingredient = default_ingredient
        self.__validator = validator if validator is not None else EnumDrinkValidator()

    def create_drink(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> IDrink:
        # This factory enforces specific brands/sizes for special editions
        if brand != EnumDrinkBrand.SPECIAL_BLEND:
            raise ValueError("SpecialEditionDrinkFactory only creates SPECIAL_BLEND drinks.")
        if size != EnumDrinkSize.COLOSSAL:
            size = EnumDrinkSize.COLOSSAL # Force colossal size for special editions

        return SpecialEditionSolidDrinks(brand, size, self.__default_ingredient, validator=self.__validator)

# --- Client Code Demonstration ---

def order_and_display_drink(factory: IDrinkFactory, brand: EnumDrinkBrand, size: EnumDrinkSize):
    """
    Client code that depends on the IDrinkFactory abstraction.
    This function DOES NOT need to change if the concrete factory type changes.
    """
    print(f"\n--- Ordering drink using factory of type: {type(factory).__name__} ---")
    try:
        drink = factory.create_drink(brand, size)
        print(f"Ordered: {drink.describe()}")
        print(f"Underlying object type: {type(drink).__name__}")
    except ValueError as e:
        print(f"Failed to order drink: {e}")
    print("-" * 50)
