#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) > 1:
        print(sum(int(arg) for arg in sys.argv[1:]))
    else:
        print(0)


if __name__ == "__main__":
    main()
