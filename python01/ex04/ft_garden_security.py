#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
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

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            print(f"Height updated: {height}cm")
            self._height = height

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {age} days")
            self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


def garden_security() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-5)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    garden_security()
