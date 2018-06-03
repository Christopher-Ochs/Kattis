import math
import sys


def main():
    target = int(sys.stdin.readline())
    temps = sys.stdin.readline().split()
    count = 0
    for t in temps:
        if int(t) < 0:
            count += 1

    sys.stdout.write(str(count))


if __name__ == "__main__":
    main()
