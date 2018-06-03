import math
import sys

def flip(str):
    newStr = ""
    newStr += str[2]
    newStr += str[1]
    newStr += str[0]
    return newStr




def main():
    array = sys.stdin.readline()
    str1 = array[0:3]
    str2 = array[4:7]
    num1 = int(flip(str1))
    num2 = int(flip(str2))

    if num1 > num2:
        sys.stdout.write(str(num1))
    else:
        sys.stdout.write(str(num2))



if __name__ == "__main__":
    main()
