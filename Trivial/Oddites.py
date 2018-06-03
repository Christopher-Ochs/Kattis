import math
import sys


def oddities():
    x = int(sys.stdin.readline())
    for i in range(0, x):
        y = int(sys.stdin.readline())
        if y % 2 == 0:
            sys.stdout.write(str(y) + " is even\n")
        else:
            sys.stdout.write(str(y) + " is odd\n")


def main():
    oddities()


if __name__ == "__main__":
    main()