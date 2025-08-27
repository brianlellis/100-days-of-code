# --- Existing SOLID Abstractions (from solid_concept.py) ---

# S: Single Responsibility Principle (SRP)
# I: Interface Segregation Principle (ISP)
# D: Dependency Inversion Principle (DIP)

class IDrinkValidator(ABC):
    """
    Abstraction for validating drink components.
    SRP: This interface defines the responsibility of validation.
    DIP: High-level classes (like SolidDrinks) will depend on this abstraction.
    """
    @abstractmethod
    def is_valid_brand(self, brand: EnumDrinkBrand) -> bool:
        pass

    @abstractmethod
    def is_valid_size(self, size: EnumDrinkSize) -> bool:
        pass

class EnumDrinkValidator(IDrinkValidator):
    """
    Concrete implementation of IDrinkValidator.
    SRP: Solely responsible for validating EnumDrinkBrand and EnumDrinkSize.
    OCP: Open for extension (e.g., adding new validation rules in a subclass), closed for modification
         (adding new enums doesn't require changing this class's methods, just the enums themselves).
    """
    def is_valid_brand(self, brand: EnumDrinkBrand) -> bool:
        return brand in EnumDrinkBrand

    def is_valid_size(self, size: EnumDrinkSize) -> bool:
        return size in EnumDrinkSize

# --- New Abstractions for Further SOLID Application ---

# Product Abstraction
class IProduct(ABC):
    """
    New abstraction for a generic product.
    This allows for a higher level of abstraction beyond just 'Drinks'.
    ISP: Defines common methods applicable to any product.
    """
    @abstractmethod
    def get_name(self) -> str:
        """Returns the name of the product."""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Returns a full description of the product."""
        pass

# Updated IDrink to inherit from IProduct
class IDrink(IProduct, ABC): # IDrink now explicitly inherits from IProduct
    """
    Abstraction for a drink, now inheriting from IProduct.
    ISP: Defines only the essential methods for a drink (get_brand, get_size).
         Clients using IDrink won't be forced to depend on validation methods.
    DIP: High-level modules (like a DrinkFactory or FluentSolidDrinks) can depend on this abstraction.
    LSP: Any concrete implementation of IDrink (like SolidDrinks) must also fulfill the IProduct contract,
         ensuring it can be substituted wherever an IProduct is expected.
    """
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

    # describe method is now inherited from IProduct and implemented in SolidDrinks

class SolidDrinks(IDrink):
    """
    A concrete implementation of IDrink, adhering to SOLID principles.
    It also now implicitly implements IProduct methods via IDrink inheritance.
    """
    def __init__(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM,
                 validator: IDrinkValidator = None):
        """
        Constructor for SolidDrinks.
        DIP: Depends on the IDrinkValidator abstraction, not a concrete validator.
             If no validator is provided, it defaults to EnumDrinkValidator.
        """
        self.__validator = validator if validator is not None else EnumDrinkValidator()

        if not self.__validator.is_valid_brand(brand):
            raise ValueError(f"Invalid drink brand: {brand}")
        self.__brand = brand

        if not self.__validator.is_valid_size(size):
            raise ValueError(f"Invalid drink size: {size}")
        self.__size = size

    # S: Single Responsibility Principle (SRP)
    # The SolidDrinks class is now primarily responsible for representing a drink's state.
    # It delegates validation to the IDrinkValidator.

    # O: Open/Closed Principle (OCP)
    # The set_brand and set_size methods now use the validator.
    # If new Enum members are added, these methods don't need to change.
    # If new validation logic is needed, create a new IDrinkValidator implementation without modifying SolidDrinks.

    # L: Liskov Substitution Principle (LSP)
    # SolidDrinks implements IDrink. Any code expecting an IDrink can safely use a SolidDrinks object.
    # Since IDrink now extends IProduct, SolidDrinks can also be substituted where an IProduct is expected.

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
        """Implements IProduct.get_name()"""
        return f"{self.__brand.name} Drink"

    def describe(self) -> str:
        """Implements IProduct.describe()"""
        return f"{self.__size.name} {self.__brand.name} Drink"

# --- Factory Abstraction ---

class IDrinkFactory(ABC):
    """
    New abstraction for creating IDrink objects.
    DIP: Client code depends on this abstraction, not concrete factory implementations.
    OCP: Open for extension (new factory types), closed for modification (client code doesn't change when factory implementation changes).
    SRP: Solely responsible for the creation of IDrink instances.
    """
    @abstractmethod
    def create_drink(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> IDrink:
        """Creates and returns an IDrink instance."""
        pass

class SolidDrinkFactory(IDrinkFactory):
    """
    Concrete implementation of IDrinkFactory, creating SolidDrinks.
    DIP: Can take an optional validator, promoting dependency inversion.
    """
    def __init__(self, validator: IDrinkValidator = None):
        self.__validator = validator if validator is not None else EnumDrinkValidator()

    def create_drink(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> IDrink:
        """
        Creates a SolidDrinks instance.
        The factory encapsulates the knowledge of which concrete IDrink to instantiate.
        """
        return SolidDrinks(brand, size, validator=self.__validator)

# --- Updated Fluent Interface for Consistency ---
# (Assumes you want to keep this pattern)

class IFluentDrinkBuilder(ABC):
    """
    Abstraction for a fluent builder for drinks.
    ISP: Clients interact with this interface to build a drink fluently.
    """
    @abstractmethod
    def set_brand(self, brand: EnumDrinkBrand):
        pass

    @abstractmethod
    def set_size(self, size: EnumDrinkSize):
        pass

    @abstractmethod
    def build(self) -> IDrink:
        pass


class FluentSolidDrinkBuilder(IFluentDrinkBuilder):
    """
    A concrete fluent builder for SolidDrinks, adhering to DIP.
    """
    def __init__(self, initial_brand: EnumDrinkBrand, initial_size: EnumDrinkSize = EnumDrinkSize.MEDIUM, validator: IDrinkValidator = None):
        """
        DIP: The builder depends on IDrinkValidator for validation, and builds an IDrink.
        It encapsulates the creation steps.
        """
        self.__validator = validator if validator is not None else EnumDrinkValidator()
        self.__brand = initial_brand
        self.__size = initial_size

    def set_brand(self, brand: EnumDrinkBrand):
        if not self.__validator.is_valid_brand(brand):
            raise ValueError(f"Invalid brand for builder: {brand}")
        self.__brand = brand
        return self # Return self for chaining

    def set_size(self, size: EnumDrinkSize):
        if not self.__validator.is_valid_size(size):
            raise ValueError(f"Invalid size for builder: {size}")
        self.__size = size
        return self # Return self for chaining

    def build(self) -> IDrink:
        """
        Builds and returns the final IDrink object.
        """
        # The builder now creates the SolidDrinks instance, using its accumulated state
        return SolidDrinks(self.__brand, self.__size, validator=self.__validator)
