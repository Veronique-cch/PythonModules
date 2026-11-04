#!/usr/bin/env python3

import sys

def create_inventory() -> dict:
    invent : dict = {}
    for i in sys.argv[1:]:
        part = i.split(":")
        if len(part) != 2:
            print(f"Error - Invalid parameter : '{i}'")
            continue
        item = part[0]
        try:
            quant = int(part[1])
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}") 
            continue
        if item in invent:
            print(f"Redundant item : '{item}' - discarding")
            continue
        invent[item] = quant
    return (invent)

def inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory : dict = create_inventory()
    print(f"Got Inventory: {inventory}")
    items : list = list(inventory.keys())
    print(f"item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    for i in items:
        percent = round((inventory[i] / total * 100), 1)
        print(f"Item {i} represents {percent}%")
    max : str = items[0]
    min : str = items[0]
    for i in items:
        if inventory[i] > inventory[max]:
            max = i
        elif inventory[i] < inventory[min]:
            min = i
    print(f"Item most abundant: {max} with quantity {inventory[max]}")
    print(f"Item least abundant: {min} with quantity {inventory[min]}")
    inventory.update({"magic_item" : 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    inventory_system()