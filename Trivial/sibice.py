import math
import sys


def Sibice():
    x = sys.stdin.readline()
    arry = x.split()
    counter = int(arry[0])
    maxLength = math.sqrt((int(arry[1]) * int(arry[1])) + (int(arry[2]) * int(arry[2])))
    while counter > 0:
        inpt = int(sys.stdin.readline())
        if counter > 0 and inpt <= maxLength:
            sys.stdout.write("DA\n")
        else:
            sys.stdout.write("NE\n")
        counter -= 1


def main():
    Sibice()


if __name__ == "__main__":
    main()
