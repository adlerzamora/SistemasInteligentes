from puzzleStruc import Puzzle
from datastructures import Queue
from collections import defaultdict
import timeit
import copy

#Basic BFS

def BFSPuzzle(startNode):
    temp = copy.deepcopy(startNode)
    myQueue = Queue()
    myQueue.enqueue(temp)
    #temp = copy.deepcopy(myQueue.dequeue())
    puzzleStateList = []
    puzzleStateList.append(temp.numbers)
    
    while myQueue.size() > 0:
        temp = myQueue.dequeue()

        temp1 = copy.deepcopy(temp) # upMovement Temp Node
        temp2 = copy.deepcopy(temp) # downMovement Temp Node
        temp3 = copy.deepcopy(temp) #leftMovement Temp Node
        temp4 = copy.deepcopy(temp) # rightMovement Temp Node

        if temp.numbers == [1,2,5,6,3,4,7,8,0]: # targetNode
            temp.toString()
            print("Arbol Genealogico")
            temp.familyTree() #BackTrace family tree route from target to root
            print(len(puzzleStateList))
            input()
        else: # looks for all possible movements and adds to the queue the ones that are not in the list yet
            if temp1.moveUp() != 0 and temp1.numbers not in puzzleStateList:
                temp1.setParent(temp)
                puzzleStateList.append(temp1.numbers)
                myQueue.enqueue(temp1)
            if temp2.moveDown() != 0 and temp2.numbers not in puzzleStateList:
                temp2.setParent(temp)
                puzzleStateList.append(temp2.numbers)
                myQueue.enqueue(temp2)
            if temp3.moveLeft() != 0 and temp3.numbers not in puzzleStateList:
                temp3.setParent(temp)
                puzzleStateList.append(temp3.numbers)
                myQueue.enqueue(temp3)
            if temp4.moveRight() != 0 and temp4.numbers not in puzzleStateList:
                temp4.setParent(temp)
                puzzleStateList.append(temp4.numbers)
                myQueue.enqueue(temp4)

def Main():
    p1 = Puzzle([0,1,2,3,4,5,6,7,8], None)  # Puzzle initial
    BFSPuzzle(p1)

if __name__ == "__main__":
    Main()
