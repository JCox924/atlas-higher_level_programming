#!/usr/bin/python3
import sys

def main():
    total_sum = 0

    for arg in sys.argv[1:]:
        total_sum += int(arg)
    print(total_sum)

if __name__ == "__main__":
    main()
