from basic_concept import EnumDrinkBrand, EnumDrinkSize


# --- SOLID Principles Application ---

# S: Single Responsibility Principle (SRP)
# I: Interface Segregation Principle (ISP)
# D: Dependency Inversion Principle (DIP) - High-level modules should not depend on low-level modules. Both should depend on abstractions.

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

# I: Interface Segregation Principle (ISP)
# L: Liskov Substitution Principle (LSP)
# D: Dependency Inversion Principle (DIP)

class IDrink(ABC):
    """
    Abstraction for a drink.
    ISP: Defines only the essential methods for a drink (get_brand, get_size).
         Clients using IDrink won't be forced to depend on validation methods.
    DIP: High-level modules (like a DrinkFactory or FluentSolidDrinks) can depend on this abstraction.
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

    @abstractmethod
    def describe(self) -> str:
        pass


class SolidDrinks(IDrink):
    """
    A concrete implementation of IDrink, adhering to SOLID principles.
    """
    def __init__(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM,
                 validator: IDrinkValidator = None):
        """
        Constructor for SolidDrinks.
        DIP: Depends on the IDrinkValidator abstraction, not a concrete validator.
             If no validator is provided, it defaults to EnumDrinkValidator.
        """
        self.__validator = validator if validator is not None else EnumDrinkValidator()

        # Input validation using the injected validator
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
    # If new Enum members are added, these methods don't need to change,
    # as the `is_valid_brand` and `is_valid_size` methods in `EnumDrinkValidator`
    # are designed to handle new enum members without modification (e.g., `brand in EnumDrinkBrand`).
    # If a new validation *logic* is needed (e.g., custom rules beyond enum membership),
    # you can create a new `IDrinkValidator` implementation without modifying `SolidDrinks`.

    # L: Liskov Substitution Principle (LSP)
    # SolidDrinks implements IDrink. Any code expecting an IDrink can safely use a SolidDrinks object,
    # and it will behave as expected according to the IDrink contract.

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

    def describe(self) -> str:
        return f"{self.__size.name} {self.__brand.name}"

