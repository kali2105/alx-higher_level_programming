#!/usr/bin/python3

if __name__ == "__main__":
    """program that print num of agrs in str"""

    import sys
    arguments = sys.argv[1:]

    num_a = len(arguments)

    if num_a == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_a, 's' if num_a > 1 else ''))
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))
