#!/usr/bin/env python3

def garden_operation(operation_number):
    print (f"Testing operation {operation_number}...")
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        3 / 0
    elif (operation_number == 2):
        open("/wtenn/ettn/agnn")
    elif (operation_number == 3):
        "abc" + 42
    else:
        print("Operation completed successfully")

def test_error_types():
    print(f"=== Garden Error Types Demo ===")
    for test in range(0, 5):
        try:
            garden_operation(test)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as error:
            print(f"Caught {type(error).__name__}: {error}")
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()