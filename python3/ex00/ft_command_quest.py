#!/usr/bin/env python3

import sys


def print_arg(arg: str, nb: int) -> None:
    print(f"Argument {nb}: {arg}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    size = len(sys.argv)
    if size == 1:
        print("No arguments provided!")
    else:
        i = 1
        print(f"Arguments received: {size - 1}")
        while size > i:
            print_arg(sys.argv[i], i)
            i += 1
    print(f"Total arguments: {size}")
