#!/usr/bin/env python3

def input_temperature (temp_str):
    print (f"\nImput data is '{temp_str}'")
    temp = int (temp_str)
    print (f"Temperature is now {temp}°C")
    return temp

def test_temperature ():
    print ("=== Garden Temperature ===")
    for test in ("25", "abc"):
        try :
            input_temperature (test)
        except ValueError as error :
            print (f"Caught input_temperature error: {error}")
    print ("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()