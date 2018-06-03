import math
import sys


def main():
    sys.stdin.readline()
    hits = sys.stdin.readline().split()
    print(hits)
    bases = 0
    count = 0
    for i in hits:
        if i != '-1':
            bases += int(i)
            count += 1

    print(bases)
    print(count)
    sys.stdout.write(str(bases/count) + '\n')


if __name__ == "__main__":
    main()

