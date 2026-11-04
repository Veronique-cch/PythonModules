#!/usr/bin/env python3

import sys

def print_arg(arg: str, n: int):
    print(f"Argument {n}: {arg}")

if __name__ == "__main__":
    size = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if size == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {size - 1}")
        i = 1
        while i < size:
            print_arg(sys.argv[i], i)
            i += 1
    print(f"Total arguments: {size}")