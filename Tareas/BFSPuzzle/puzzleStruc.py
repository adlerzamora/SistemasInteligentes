class Puzzle:
    def __init__(self, numbers, parent):
        self.numbers = numbers
        self.parent = parent
        self.setZeroIndex()

    def setZeroIndex(self):
        try:
            self.zeroIndex = self.numbers.index(0)
        except ValueError:
            self.zeroIndex = -1

    def setParent(self, parent):
        self.parent = parent

    def toString(self):
        print("["+str(self.numbers[0])+"|"+str(self.numbers[1])+"|"+str(self.numbers[2])+"]")
        print("["+str(self.numbers[3])+"|"+str(self.numbers[4])+"|"+str(self.numbers[5])+"]")
        print("["+str(self.numbers[6])+"|"+str(self.numbers[7])+"|"+str(self.numbers[8])+"]")
        print("---------------")
            
    def moveUp(self):
        self.setZeroIndex()
        if self.zeroIndex > 2:
           self.swapValues(self.zeroIndex - 3, self.zeroIndex)
           self.setZeroIndex()
           return 1
        else:
            return 0

    def moveDown(self):
        self.setZeroIndex()
        if self.zeroIndex < 6:
            self.swapValues(self.zeroIndex, self.zeroIndex + 3)
            self.setZeroIndex()
            return 1
        else:
            return 0

    def moveLeft(self):
        self.setZeroIndex()
        if self.zeroIndex != 0 and self.zeroIndex != 3 and self.zeroIndex != 6:
            self.swapValues(self.zeroIndex - 1, self.zeroIndex)
            self.setZeroIndex()
            return 1
        else:
            return 0

    def moveRight(self):
        self.setZeroIndex()
        if self.zeroIndex != 2 and self.zeroIndex != 5 and self.zeroIndex != 8:
            self.swapValues(self.zeroIndex, self.zeroIndex + 1)
            self.setZeroIndex()
            return 1
        else:
            return 0
 
    def swapValues(self, a, b):
        temp = self.numbers[a]
        self.numbers[a] = self.numbers[b]
        self.numbers[b] = temp
        
    def familyTree(self):
        self.toString()
        if self.parent != None:
            self.parent.familyTree()