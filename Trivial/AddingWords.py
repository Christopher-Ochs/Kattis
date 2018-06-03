import math
import sys

class History:

    def __init__(self):
        self.keys = []
        self.values = []

    def addDef(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def lookUpKey(self, value):
        if value in self.values:
            ind = self.values.index(value)
        else:
            return 'unknown'
        return self.keys[ind]

    def lookUpValue(self, key):
        if key in self.keys:
            ind = self.keys.index(key)
        else:
            return 'unknown'
        return self.values[ind]

    def calc(self, command):
        total = 0
        for i in range(2, len(command)):
            if (command[i] == '+' or command[i] == '-') and self.lookUpValue(command[i - 1]) == 'unknown':
                return 'unknown'
            if command[i] == '+':
                total = total + int(self.lookUpValue(command[i-1]))
            if command[i] == '-':
                total = total - int(self.lookUpValue(command[i-1]))
        return str(self.lookUpKey(total))



def main():
    command = sys.stdin.readline().split()
    hist = History()

    while command[0] != 'clear':
        print(command)
        if command[0] == 'def':
            hist.addDef(command[1], command[2])
        if command[0] == 'key':
            hist.lookUpValue(command[1])
        if command[0] == 'value:':
            hist.lookUpKey(command[1])
        if command[0] == 'calc':
            for i in command[1:]:
                sys.stdout.write(i + ' ')
            sys.stdout.write(hist.calc(command) + '\n')
        command = sys.stdin.readline().split()



if __name__ == "__main__":
    main()

