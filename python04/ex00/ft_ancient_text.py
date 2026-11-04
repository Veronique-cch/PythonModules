#!/usr/bin/env python3

import sys

def ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        file = None
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            print(f"---\n\n{content}\n\n---")
        except Exception as error:
            print(f"Error opening file '{sys.argv[1]}': {error}")
        finally:
            if file:
                file.close()
                print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    ancient_text()