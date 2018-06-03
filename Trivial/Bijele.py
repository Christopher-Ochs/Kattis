import math
import sys


def main():
    starting = sys.stdin.readline().split()
    goal = [1, 1, 2, 2, 2, 8]
    for i in range(0, len(goal)):
        goal[i] -= int(starting[i])

    for x in goal:
        sys.stdout.write(str(x) + ' ')


if __name__ == "__main__":
    main()

