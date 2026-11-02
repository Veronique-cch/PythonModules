#!/usr/bin/env python3

class GardenError(ValueError):
    def __init__(self, msg="Unknown garden error"):
        self.msg = msg
        super().__init__(self.msg)

class PlantError(GardenError):
    def __init__(self, msg="Unknown plant error"):
        self.msg = msg
        super().__init__(self.msg)

def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError (f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")

def test_watering_system():
    print("\nTesting valid plant...")
    print("Opening watering system")
    plants = ["Tomato", "Lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caugth PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    plants = ["Tomato", "lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(f".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    

if __name__== "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")