import math
import sys


def listOfInts(row):
    x = []
    for i in row:
        x.append(int(i))
    return x


def compare(numbers):
    count = 0
    for i in range(0, len(numbers)):
        num1 = numbers[i]
        for j in range(i, len(numbers)):
            num2 = numbers[j]
            if i != j and (num1 + num2) in numbers:
                count = count + 2

    return count


def main():
    sys.stdin.readline()
    numbers = listOfInts(sys.stdin.readline().split())
    sys.stdout.write(str(compare(numbers)) + '\n')


if __name__ == "__main__":
    main()

