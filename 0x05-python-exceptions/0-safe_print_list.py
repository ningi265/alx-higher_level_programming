#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass  # Ignore index errors when x is greater than the length of my_list
    finally:
        print()  # Print a new line after the elements
        return count
