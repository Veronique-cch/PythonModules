#!/usr/bin/env python3

def garden_operations(operation_number):
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int ("abc") 
    elif operation_number == 1:
        3 / 0
    elif operation_number == 2:
        open("/naer/etea/rtg")
    elif operation_number == 3:
        ("error") + 42
    else:
        print ("Operation completed successfully")

def test_error_types():
    print ("=== Garden Error Types Demo ===")
    for test in range(0, 5):
        print 
        try:
            garden_operations(test)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print (f"Caught{type(e).__name__}: {e}")
    print ("\n\nAll error types tested successfully!")
    
if __name__ == "__main__":
    test_error_types()