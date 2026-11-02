#!/usr/bin/env python3

def test_temperature() -> int:
    print("=== Garden Temperature ===")
    for test in ("25", "abc"):
        try:
            input_temperature(test)
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")
 

def input_temperature(temp_str) -> None:
    print(f"\nInput data is '{temp_str}'")
    temp = int(temp_str)
    print(f"Temperature is now {temp}°C")
    return temp

if __name__ == "__main__":
    test_temperature()