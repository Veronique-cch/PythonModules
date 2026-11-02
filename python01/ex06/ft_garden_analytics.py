#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()
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

    class Stats:
        def __init__(self) -> None:
            self.grow = 0
            self.age = 0
            self.show = 0

        def display(self) -> None:
            print(f"Stats: {self.grow} grow, {self.age} age, {self.show} show")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

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
        self._stats.grow += 1

    def age_up(self) -> None:
        self._age += 1
        self._stats.age += 1

    def show(self) -> None:
        self._stats.show += 1
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def show_stats(self) -> None:
        print(f"[statistics for {self.name}]")
        self._stats.display()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return (cls("Unknown plant", 0.0, 0, 0.0))


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

    def grow_and_bloom(self, days: int) -> None:
        for i in range(days):
            self.grow()
        self.bloomed = True
        print(f"[asking {self.name.lower()} to grow and bloom]")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, color: str, nbseeds: int) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self.nbseeds = nbseeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.nbseeds}")

    def age_grow_and_bloom(self, days: int, nbseeds: int) -> None:
        self._age += days
        self._height += self.growth_rate * days

        self._stats.age += 1
        self._stats.grow += 1

        self.bloomed = True
        self.nbseeds = nbseeds
        print(f"[make {self.name.lower()} grow, age and bloom]")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = Tree.Stats()

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade = 0

        def display(self) -> None:
            super().display()
            print(f" {self.shade} shade")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of",
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        self._stats.shade += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def show_stats(self) -> None:
        super().show_stats()


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

    def age_and_grow(self, days: int) -> None:
        for i in range(days):
            self.age_up()
            self.grow()
            self.nutritional_value += 1
        print(f"[make {self.name.lower()} grow and age for {days} days]")


def display_stats(plant) -> None:
    plant.show_stats()


def garden_analytics():
    rose = Flower("Rose", 15.0, 10, 8, "red")
    oak = Tree("Oak", 200.0, 365, 1, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, 1.5, "yellow", 0)
    unknown = Plant.anonymous()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(" Is 30 days more than a year? ->", Plant.is_older_than_year(30))
    print(" Is 400 days more than a year? ->", Plant.is_older_than_year(400))
    print()
    print("=== Flower")
    rose.show()
    display_stats(rose)
    rose.grow_and_bloom(1)
    rose.show()
    display_stats(rose)
    print()
    print("=== Tree")
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print()
    print("=== Seed")
    sunflower.show()
    sunflower.age_grow_and_bloom(20, 42)
    sunflower.show()
    display_stats(sunflower)
    print()
    print("=== Anonymous")
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    garden_analytics()
