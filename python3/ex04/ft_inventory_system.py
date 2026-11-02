#!/usr/bin/env python3

import sys

def create_invetory() -> dict:
    inventory = {}
    for i in sys.args:
        try:
            args = i.split(":")
            if len(args) != 2:
                print(f"Error - Invalid parameter '{i}'")
            index = str(args[0])
            value = int(args[1])
            if index in inventory:
                print(f"Redundant item '{index}' - discarding")
                continue
            else:
                inventory[index] = value
        except ValueError as e:
            print(f"Quantity error for 'key' = {e}")
        return inventory

def inventory_system() -> None:
    inventory = create_inventory()
    print(f"Got inventory: {inventory}")
    

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")