#!/usr/bin/env python3

import sys


def av(scores: list) -> float:
    return sum(scores) / len(scores)


def print_stats(scores: list[int]) -> None:
    size = len(scores)
    average = av(scores)
    summ = sum(scores)
    high = max(scores)
    low = min(scores)
    rge = high - low
    print(f"Scores processed: {scores}")
    print(f"Total players: {size}")
    print(f"Total score: {summ}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {rge}\n")


def ft_scores_analytics() -> None:
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...\n")
    else:
        args = []
        for i in sys.argv[1:]:
            try:
                args.append(int(i))
            except ValueError:
                print(f"Invalid parameter: '{i}'")
        if len(args) == 0:
            print("No scores provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...\n")
        else:
            print_stats(args)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_scores_analytics()
