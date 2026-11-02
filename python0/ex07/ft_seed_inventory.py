def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "area":
        print(seed_type.capitalize(), "seeds:", quantity, "square meters")
    elif unit == "packets":
        print(seed_type.capitalize(), "seeds:", quantity, unit, "available")
    elif unit == "grams":
        print(seed_type.capitalize(), "seeds:", quantity, unit, "total")
    else:
        print("Unknow unit type")
