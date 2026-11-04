#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown plant error!"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error!"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown plant error!"):
        super().__init__(message)

def test_errors():
    print(=== Custom Garden Errors Demo ===)