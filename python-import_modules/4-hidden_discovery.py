#!/usr/bin/python3
import hidden_4

def print_sorted_names():
    names = dir(hidden_4)
    for name in sorted:
		if name[:2] != "__":
			print(name)

if __name__ == "__main__":
    print_sorted_names()
