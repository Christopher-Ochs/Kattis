import math
import sys


def main():
    sentence = sys.stdin.readline().split()
    duplicate = False
    for i in sentence:
        temp = sentence
        temp.remove(i)
        if i in temp:
            duplicate = True

    if duplicate:
        sys.stdout.write("no\n")
    else:
        sys.stdout.write("yes\n")


if __name__ == "__main__":
    main()

