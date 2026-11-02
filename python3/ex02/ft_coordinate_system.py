#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z':")
        pos = coords.split(',')

        if len(pos) != 3:
            print("Invalid syntax")
            continue
        tupp = []
        is_error = False
        for i in pos:
            try:
                i = i.strip()
                tupp.append(float(i))
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                is_error = True
                break

        if is_error:
            continue
        return tuple(tupp)


def calculate_distance(pos_a: tuple, pos_b: tuple) -> float:
    x_a = pos_a[0]
    x_b = pos_b[0]
    y_a = pos_a[1]
    y_b = pos_b[1]
    z_a = pos_a[2]
    z_b = pos_b[2]

    dist = math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2 + (z_b - z_a)**2)
    return dist


def coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It include: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist_to_center = round(calculate_distance(pos1, (0, 0, 0)), 4)
    print(f"Distance to center: {dist_to_center}\n")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist_2 = round(calculate_distance(pos1, pos2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist_2}")


if __name__ == "__main__":
    coordinate_system()
