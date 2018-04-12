import math
import sys


def quadrantSelection():
    x = int(sys.stdin.readline())
    y = int(sys.stdin.readline())
    if x > 0:
        if y > 0:
            sys.stdout.write("1")
        else:
            sys.stdout.write("4")
    elif y > 0:
        sys.stdout.write("2")
    else:
        sys.stdout.write("3")



def main():
    quadrantSelection()


if __name__ == "__main__":
    main()