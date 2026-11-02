#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: list, number: int) -> set[str]:
    choice = random.sample(achievements, number)
    return set(choice)


def achievement_traker():
    achievements = [
        "Crafting Genius", "World Saver", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Unstoppable", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind"]

    alice = gen_player_achievements(achievements, random.randint(4, 9))
    bob = gen_player_achievements(achievements, random.randint(4, 9))
    charlie = gen_player_achievements(achievements, random.randint(4, 9))
    dylan = gen_player_achievements(achievements, random.randint(4, 9))
    all_achievement = set(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"\nAll Distinct achievements: "
          f"{set.union(alice, bob, charlie, dylan)}")
    print(f"Commom Achievement: {alice.intersection(bob, charlie, dylan)}")
    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print(f"\nAlice is missing: {all_achievement.difference(alice)}")
    print(f"Bob is missing: {all_achievement.difference(bob)}")
    print(f"Charlie is missing: {all_achievement.difference(charlie)}")
    print(f"Dylan is missing: {all_achievement.difference(dylan)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievement_traker()
