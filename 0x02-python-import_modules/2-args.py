#!/usr/bin/python3

if __name__ == "__main__":
    """program that print num of agrs in str"""
    
    import sys
    arguments = sys.argv[1:]

    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_arguments, 's' if num_arguments > 1 else ''))
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))

