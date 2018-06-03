import math
import sys


def main():
    word = sys.stdin.readline()
    hiss = False

    for i in range(0, len(word[1:])):
        if (word[i] == 's') and (word[i+1] == 's'):
            hiss = True

    if hiss:
        sys.stdout.write("hiss\n")
    else:
        sys.stdout.write("no hiss\n")


if __name__ == "__main__":
    main()