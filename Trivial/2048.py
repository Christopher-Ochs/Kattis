import math
import sys


def rotateMatrix(matrix):
    newMatrix = []
    for x in range(0, len(matrix)):
        column = []
        for y in range(0, len(matrix)):
            column.append(matrix[y][x])
        newMatrix.append(column)
    return newMatrix


def slideRowRight(row):
    while 0 in row:
        row.remove(0)
    if len(row) >= 4 and row[0] == row[1] and row[2] == row[3]:
        row[0] = row[0]*2
        row[2] = row[2]*2
        row[1] = 0
        row[3] = 0
    elif len(row) >= 4 and row[2] == row[3]:
        row[2] = row[2] * 2
        row[3] = 0
    elif len(row) >= 3 and row[1] == row[2]:
        row[1] = row[1] * 2
        row[2] = 0
    elif len(row) >= 2 and row[0] == row[1]:
        row[0] = row[0] * 2
        row[1] = 0
    while 0 in row:
        row.remove(0)
    while len(row) != 4:
        row = [0] + row
    return row


def slideRowleft(row):
    while 0 in row:
        row.remove(0)
    if len(row) >= 4 and row[0] == row[1] and row[2] == row[3]:
        row[0] = row[0]*2
        row[2] = row[2]*2
        row[1] = 0
        row[3] = 0
    elif len(row) >= 2 and row[0] == row[1]:
        row[0] = row[0]*2
        row[1] = 0
    elif len(row) >= 3 and row[1] == row[2]:
        row[1] = row[1]*2
        row[2] = 0
    elif len(row) >= 4 and row[2] == row[3]:
        row[2] = row[2]*2
        row[3] = 0
    while 0 in row:
        row.remove(0)
    while len(row) != 4:
        row.append(0)
    return row


def slideMatrixLeft(matrix):
    matrix[0] = slideRowleft(matrix[0])
    matrix[1] = slideRowleft(matrix[1])
    matrix[2] = slideRowleft(matrix[2])
    matrix[3] = slideRowleft(matrix[3])
    return matrix


def slideMatrixRight(matrix):
    matrix[0] = slideRowRight(matrix[0])
    matrix[1] = slideRowRight(matrix[1])
    matrix[2] = slideRowRight(matrix[2])
    matrix[3] = slideRowRight(matrix[3])
    return matrix


def slideMatrixUp(matrix):
    matrix = rotateMatrix(matrix)
    matrix = slideMatrixLeft(matrix)
    matrix = rotateMatrix(matrix)
    return matrix


def slideMatrixDown(matrix):
    matrix = rotateMatrix(matrix)
    matrix = slideMatrixRight(matrix)
    matrix = rotateMatrix(matrix)
    return matrix


def printMatrix(matrix):
    for i in matrix:
        for j in i:
            sys.stdout.write(str(j) + ' ')
        sys.stdout.write('\n')


def listOfInts(row):
    x = []
    for i in row:
        x.append(int(i))
    return x


def move(direction, matrix):
    if direction == 0:
        return slideMatrixLeft(matrix)
    if direction == 1:
        return slideMatrixUp(matrix)
    if direction == 2:
        return slideMatrixRight(matrix)
    if direction == 3:
        return slideMatrixDown(matrix)


def main():
    row1 = listOfInts(sys.stdin.readline().split())
    row2 = listOfInts(sys.stdin.readline().split())
    row3 = listOfInts(sys.stdin.readline().split())
    row4 = listOfInts(sys.stdin.readline().split())
    matrix = [row1, row2, row3, row4]
    direction = int(sys.stdin.readline())
    matrix = move(direction, matrix)
    printMatrix(matrix)


if __name__ == "__main__":
    main()

