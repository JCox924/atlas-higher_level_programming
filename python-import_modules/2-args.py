#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]  # Exclude the script name from the arguments list
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "s" if argc > 1 else ""))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
