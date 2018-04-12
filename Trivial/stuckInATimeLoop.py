import sys


def looper():
    x = sys.stdin.readline()
    for i in range(1, int(x)+1):
        sys.stdout.write(str(i) + " Abracadabra\n")


def main():
    looper()


if __name__ == "__main__":
    main()
