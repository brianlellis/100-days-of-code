from basic_concept import EnumDrinkBrand, EnumDrinkSize


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
        """Returns the name of the product."""
        pass

    @abstractmethod
    def describe(self) -> str:
        """Returns a full description of the product."""
        pass


class IDrink(IProduct, ABC): # IDrink now explicitly inherits from IProduct
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
        """Implements IProduct.get_name()"""
        return f"{self.__brand.name} Drink"

    def describe(self) -> str:
        """Implements IProduct.describe()"""
        return f"{self.__size.name} {self.__brand.name} Drink"


class IDrinkFactory(ABC):
    @abstractmethod
    def create_drink(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> IDrink:
        """Creates and returns an IDrink instance."""
        pass

class SolidDrinkFactory(IDrinkFactory):
    def __init__(self, validator: IDrinkValidator = None):
        self.__validator = validator if validator is not None else EnumDrinkValidator()

    def create_drink(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM) -> IDrink:
        return SolidDrinks(brand, size, validator=self.__validator)
