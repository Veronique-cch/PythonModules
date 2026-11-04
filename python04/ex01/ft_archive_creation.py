#!/usr/bin/env python3

import sys

def show_file() -> str | None:
    content = None
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
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
        return content


def save_file(content: str) -> None:
    new_name = str(input("Enter new file name (or empty):"))
    if not new_name:
        print("Not saving data.")
        return
    try:
        print(f"Saving data to '{new_name}'")
        file = open(new_name, "w")
        file.write(content)
        print(f"Data saved in file '{new_name}'.")
    except Exception as error:
        print(f"Error opening file: {error}")

def archive_creation() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    content = show_file()
    if not content:
        return
    content_new_line = [line + "#" for line in content.splitlines()]
    content = "\n".join(content_new_line) + "\n"
    print("\nTransform data:")
    print(f"---\n\n{content}\n\n---")
    save_file(content)

if __name__ == "__main__":
    archive_creation()