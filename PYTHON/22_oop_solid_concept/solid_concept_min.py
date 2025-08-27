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


class IDrink(ABC):
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
    def __init__(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM,
                 validator: IDrinkValidator = None):
        self.__validator = validator if validator is not None else EnumDrinkValidator()

        # Input validation using the injected validator
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

    def describe(self) -> str:
        return f"{self.__size.name} {self.__brand.name}"

