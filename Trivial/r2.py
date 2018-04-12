import math
import sys


def r2():
    x = sys.stdin.readline()
    arry = x.split()
    num1 = int(arry[0])
    num2 = int(arry[1])
    num3 = (num2-num1) + num2
    sys.stdout.write(str(num3))


def main():
    r2()


if __name__ == "__main__":
    main()