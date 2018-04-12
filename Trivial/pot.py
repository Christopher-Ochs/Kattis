import math
import sys


def pot():
    x = int(sys.stdin.readline())
    sum = 0
    while x > 0:
        y = sys.stdin.readline()
        num = int(y[:-2])
        power = int(y[-2])
        sum += int(math.pow(num, power))
        x -= 1
    sys.stdout.write(str(sum))


def main():
    pot()


if __name__ == "__main__":
    main()