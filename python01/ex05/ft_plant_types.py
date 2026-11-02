#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self.growth_rate = growth_rate
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            print(f"Height updated: {height}cm")
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {age} days")
            self._age = age

    def grow(self) -> None:
        self._height += self.growth_rate

    def age_up(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of",
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, harvest_season: str) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age_up(self) -> None:
        super().age_up()
        self.nutritional_value += 1

    def age_and_grow(self, days: int) -> None:
        for i in range(days):
            self.age_up()
            self.grow()
        print(f"[make {self.name.lower()} grow and age for {days} days]")


def plant_types() -> None:
    rose = Flower("Rose", 15.0, 10, 1, "red")
    oak = Tree("Oak", 200.0, 365, 1, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    tomato.age_and_grow(20)
    tomato.show()


if __name__ == "__main__":
    plant_types()
