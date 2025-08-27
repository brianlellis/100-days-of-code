from enum import Enum


"""
Handles all parts of the drink creation.
0. Enum
1. Concrete class
2. Fluent Interface implementation
"""
class EnumDrinkBrand(Enum):
    COKE = 1
    PEPSI = 2
    SPRITE = 3

class EnumDrinkSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Drinks:
    # ctors
    def __init__(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM):
        self.setBrand(brand)
        self.setSize(size)


    # set/get Brand
    def setBrand(self, brand: EnumDrinkBrand):
        match brand:
            case EnumDrinkBrand.COKE | EnumDrinkBrand.PEPSI | EnumDrinkBrand.SPRITE:
                self.__brand = brand
            case _:
                print("Invalid drink selection.") # Unmatched/Default behavior


    def getBrand(self):
        print(f"Drink Brand: {EnumDrinkBrand(self.__brand.value).name}")


    # set/get Size
    def setSize(self, size: EnumDrinkSize):
        match size:
            case EnumDrinkSize.SMALL | EnumDrinkSize.MEDIUM | EnumDrinkSize.LARGE:
                self.__size = size
            case _:
                print("Invalid drink selection.") # Unmatched/Default behavior


    def getSize(self):
        print(f"Drink Size: {EnumDrinkSize(self.__size.value).name}")


class FluentDrinks:
    def __init__(self, brand: EnumDrinkBrand, size: EnumDrinkSize = EnumDrinkSize.MEDIUM):
        self.__drink = Drinks(brand, size)


    def setBrand(self, brand: EnumDrinkBrand):
        self.__drink.setBrand(brand)
        return self


    def getbrand(self):
        self.__drink.getBrand()

