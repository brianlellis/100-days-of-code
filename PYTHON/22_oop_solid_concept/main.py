from basic_concept import (EnumDrinkBrand, EnumDrinkSize, Drinks, FluentDrinks)

# basic class implementation
drink = Drinks(EnumDrinkBrand.COKE)
drink.setBrand(EnumDrinkBrand.PEPSI)
drink.getBrand()

# fluent interface implementation
drink2 = FluentDrinks(EnumDrinkBrand.COKE)
drink2.setBrand(EnumDrinkBrand.SPRITE).getbrand()

# ----------------------
# --- Usage "SOLID1" ---
# ----------------------

# print("--- Original Drinks Class Demonstration ---")
# drink_orig = Drinks(EnumDrinkBrand.COKE)
# drink_orig.getBrand()
# drink_orig.getSize()
# drink_orig_fluent = FluentDrinks(EnumDrinkBrand.PEPSI)
# drink_orig_fluent.setBrand(EnumDrinkBrand.SPRITE).getbrand()
# print("-" * 30)

# print("\n--- SOLID Drinks Class Demonstration ---")

# # Using the SolidDrinks with default validator
# print("Creating a SolidDrink (COKE, MEDIUM) with default validator:")
# solid_drink1 = SolidDrinks(EnumDrinkBrand.COKE)
# print(f"Solid Drink 1: {solid_drink1.describe()}")
# solid_drink1.set_size(EnumDrinkSize.LARGE)
# print(f"Solid Drink 1 (after size change): {solid_drink1.describe()}")
# print("-" * 30)

# # Demonstrating OCP: Adding a new brand/size without modifying SolidDrinks
# print("\nDemonstrating OCP: Using new Enum members (FANTA, XL) without changing SolidDrinks code:")
# solid_drink2 = SolidDrinks(EnumDrinkBrand.FANTA, EnumDrinkSize.XL)
# print(f"Solid Drink 2: {solid_drink2.describe()}")
# print("-" * 30)

# # Demonstrating SRP and DIP: Invalid input handled by validator
# print("\nDemonstrating SRP & DIP: Invalid brand/size handled by validator:")
# try:
#     # This will raise a ValueError because the validator will catch it
#     invalid_brand_enum = Enum('InvalidBrand', {'BAD': 99}) # Create a dummy invalid enum
#     solid_drink_invalid = SolidDrinks(invalid_brand_enum.BAD)
# except ValueError as e:
#     print(f"Error creating SolidDrink with invalid brand: {e}")

# try:
#     invalid_size_enum = Enum('InvalidSize', {'TINY': 0})
#     solid_drink_invalid_size = SolidDrinks(EnumDrinkBrand.COKE, invalid_size_enum.TINY)
# except ValueError as e:
#     print(f"Error creating SolidDrink with invalid size: {e}")
# print("-" * 30)

# # Demonstrating DIP with FluentSolidDrinks
# print("\n--- Fluent SOLID Drinks Demonstration (DIP) ---")
# # FluentSolidDrinks now depends on IDrink, not a concrete SolidDrinks
# initial_solid_drink = SolidDrinks(EnumDrinkBrand.SPRITE, EnumDrinkSize.SMALL)
# fluent_solid_drink = FluentSolidDrinks(initial_solid_drink)

# print(f"Initial Fluent Solid Drink: {fluent_solid_drink.describe()}")
# fluent_solid_drink.set_brand(EnumDrinkBrand.FANTA).set_size(EnumDrinkSize.LARGE)
# print(f"Fluent Solid Drink (after chaining): {fluent_solid_drink.describe()}")
# print(f"Underlying SolidDrink object also updated: {initial_solid_drink.describe()}")
# print("-" * 30)

# ----------------------
# --- Usage "SOLID2" ---
# ----------------------

# print("--- Demonstration of Further Abstraction ---")

# # 1. Using the Drink Factory (DIP, SRP, OCP)
# print("\nUsing the IDrinkFactory:")
# drink_factory: IDrinkFactory = SolidDrinkFactory() # Client depends on IDrinkFactory
# cola = drink_factory.create_drink(EnumDrinkBrand.COKE, EnumDrinkSize.LARGE)
# print(f"Created via Factory: {cola.describe()} (Type: {type(cola).__name__})")

# sprite = drink_factory.create_drink(EnumDrinkBrand.SPRITE) # Default size
# print(f"Created via Factory: {sprite.describe()}")
# print("-" * 30)

# # 2. Using IProduct abstraction (LSP)
# print("\nDemonstrating IProduct (LSP):")
# # A list of IProducts can hold different concrete product types (if we had them)
# # For now, it holds IDrinks, which are also IProducts.
# products: list[IProduct] = []
# products.append(cola)
# products.append(SolidDrinks(EnumDrinkBrand.FANTA, EnumDrinkSize.MEDIUM)) # Can still directly instantiate if needed

# for product in products:
#     print(f"Product Name: {product.get_name()}, Description: {product.describe()}")
# print("-" * 30)


# # 3. Using the Fluent Builder (SRP, DIP for construction)
# print("\nUsing the FluentSolidDrinkBuilder:")
# # The builder is responsible for assembling the drink
# builder = FluentSolidDrinkBuilder(EnumDrinkBrand.PEPSI, EnumDrinkSize.SMALL)
# energy_drink = builder.set_brand(EnumDrinkBrand.FANTA).set_size(EnumDrinkSize.XL).build()

# print(f"Built via Fluent Builder: {energy_drink.describe()}")
# print("-" * 30)

# try:
#     # Attempt to build with invalid data using the builder
#     invalid_builder = FluentSolidDrinkBuilder(Enum('Dummy', {'BAD': 99}).BAD)
# except ValueError as e:
#     print(f"Error caught using builder with invalid brand: {e}")

# try:
#     invalid_builder_size = FluentSolidDrinkBuilder(EnumDrinkBrand.COKE).set_size(Enum('Dummy', {'BAD_SIZE': 99}).BAD_SIZE)
#     invalid_drink = invalid_builder_size.build()
# except ValueError as e:
#     print(f"Error caught using builder with invalid size: {e}")


# ----------------------
# --- Usage "SOLID3" ---
# ----------------------

# # Case 1: Using the standard SolidDrinkFactory
# print("Scenario 1: Using the SolidDrinkFactory")
# standard_factory = SolidDrinkFactory()
# order_and_display_drink(standard_factory, EnumDrinkBrand.COKE, EnumDrinkSize.MEDIUM)
# order_and_display_drink(standard_factory, EnumDrinkBrand.FANTA, EnumDrinkSize.LARGE)


# # Case 2: Using the SpecialEditionDrinkFactory
# print("\nScenario 2: Using the SpecialEditionDrinkFactory")
# special_factory = SpecialEditionDrinkFactory(default_ingredient="Dragon's Breath")
# order_and_display_drink(special_factory, EnumDrinkBrand.SPECIAL_BLEND, EnumDrinkSize.COLOSSAL) # Valid special edition
# order_and_display_drink(special_factory, EnumDrinkBrand.COKE, EnumDrinkSize.MEDIUM) # Invalid for this factory