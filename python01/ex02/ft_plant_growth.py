#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def plant_growth() -> None:
    rose = Plant("Rose", 25.0, 30, 0.8)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()

    for days in range(7):
        rose.grow()
        rose.age_up()
        print(f"=== Day {days + 1} ===")
        rose.show()

    growth = round(rose.height - initial_height, 2)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    plant_growth()
