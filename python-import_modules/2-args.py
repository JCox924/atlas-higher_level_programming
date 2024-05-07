#!/usr/bin/python3
import sys

def main():
    argv = sys.argv
    num_args = len(argv) - 1  # exclude the script name itself

    if num_args == 0:
        print("arguments: 0.", end='')
    else:
        if num_args == 1:
            print("argument: 1:", end='')
        else:
            print("arguments: {}:".format(num_args), end='')
        
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]), end='')

if __name__ == "__main__":
    main()
