#!/usr/bin/env python3

class GardenError(ValueError):
    def __init__(self, msg="Unknown garden error"):
        self.msg = msg
        super().__init__(self.msg)

class PlantError(GardenError):
    def __init__(self, msg="Unknown plant error"):
        self.msg = msg
        super().__init__(self.msg)

class WaterError(GardenError):
    def __init__(self, msg="Unknown water error" ):
            self.msg = msg
            super().__init__(self.msg)


def test_customs():
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
         print(f"Caught PlantError: {error}")
    print ("\nTesting WaterError...")
    try:
        raise WaterError("Not enought water in the tank!")
    except WaterError as error:
         print(f"Caught WaterError: {error}")

def test_all_errors():
    print("\nTestind catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
         print(f"Caught GardenError: {error}")
    try:
        raise WaterError("Not enought water in the tank!")
    except GardenError as error:
         print(f"Caught GardenError: {error}")

if __name__ == "__main__":
    print("=== Custom Garden Error Demo ===")
    test_customs()
    test_all_errors()
    print("\nAll custom error types work correctly!")