import math
import sys


def main():
    array = sys.stdin.readline()
    array = array.split()
    num1 = int(array[0])
    num2 = int(array[1])
    answer = (num1 * (num2-1)) + 1

    sys.stdout.write(str(answer))


if __name__ == "__main__":
    main()
