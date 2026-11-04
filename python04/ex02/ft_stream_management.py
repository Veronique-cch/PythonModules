#!/usr/bin/env python3

import sys

def show_file() -> str | None:
    content = None
    if len(sys.argv) != 2:
        sys.stderr.write(f"[STDERR] Usage: {sys.argv[0]} <file>\n")
    else:
        file = None
        sys.stdout.write(f"Accessing file '{sys.argv[1]}'\n")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            sys.stdout.write(f"---\n\n{content}\n\n---")
        except Exception as error:
            sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {error}\n")
        finally:
            if file:
                file.close()
                sys.stdout.write(f"\nFile '{sys.argv[1]}' closed.\n")
    return content


def save_file(content: str) -> None:
    file = None
    sys.stdout.write("Enter new file name (or empty):")
    sys.stdout.flush()
    new_name = sys.stdin.readline().strip()
    if not new_name:
        sys.stdout.write("Not saving data.\n")
        return
    try:
        sys.stdout.write(f"Saving data to '{new_name}'\n")
        file = open(new_name, "w")
        file.write(content)
        sys.stdout.write(f"Data saved in file '{new_name}'.\n")
    except Exception as error:
        sys.stderr.write(f"[STDERR] Error opening file '{new_name}': {error}\n")
        sys.stdout.write("Data not saved.\n")
    finally:
        if file:
            file.close()

def archive_creation() -> None:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    content = show_file()
    if not content:
        return
    content_new_line = [line + "#" for line in content.splitlines()]
    content = "\n".join(content_new_line) + "\n"
    sys.stdout.write("\nTransform data:\n")
    sys.stdout.write(f"---\n\n{content}\n\n---")
    save_file(content)

if __name__ == "__main__":
    archive_creation()