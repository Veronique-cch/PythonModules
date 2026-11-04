#!/usr/bin/env python3

import random

def data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    players =  ["Alice", "bob", "Charlie", "dylan", "Emma",
                "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")
    capitalized_players = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_players}")
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list with capitalized names only: {capitalized_only}\n")
    score_players: dict = {name: random.randint(1, 1000)
                          for name in capitalized_players}
    print(f"Score dict: {score_players}")
    average : float = round(sum(score_players.values()) / len(score_players), 2)
    print(f"Score average is {average}")
    high_scores : dict = {
            name : score 
            for name, score in score_players.items() 
            if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    data_alchemist()