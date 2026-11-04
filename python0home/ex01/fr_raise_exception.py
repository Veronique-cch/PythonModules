#!/usr/bin/env python3

def input_temperature (temp_str):
    print (f"\nImput data is '{temp_str}'")
    temp = int (temp_str)
    if temp < 0:
        raise ValueError (f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError (f"{temp}°C is too hot for plants (max 40°C)")
    else :
        print (f"Temperature is now {temp}°C")
        return temp

def test_temperature ():
    print ("=== Garden Temperature Checker ===")
    for test in ("25", "abc", "100", "-50"):
        try :
            input_temperature (test)
        except ValueError as error :
            print (f"Caught input_temperature error: {error}")
    print ("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()