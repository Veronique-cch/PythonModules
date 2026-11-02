#!/usr/bin/env python3

def test_temperature() -> int:
    for test in ("25", "abc", "100", "-50"):
        try:
            input_temperature(test)
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


def input_temperature(temp_str) -> None:
    print(f"\nInput data is '{temp_str}'")
    temp = int(temp_str)
    if (temp < 0):
        raise ValueError(f"{temp}°C is to cold for plants (min 0°C)")
    elif (temp > 40):
        raise ValueError(f"{temp}°C is too hot fot plants (max 40°C)")
    else:
        print(f"Temperature is now {temp}°C")
        return temp


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
