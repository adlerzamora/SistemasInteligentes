class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        #Checking to avoid duplicate entries
        if data not in self.queue:
            self.queue.append(data)
            return True
        else:
            return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return "Queue Empty"

    def size(self):
        return len(self.queue)


#def Main():
#    myQueue = Queue()
#    print(myQueue.enqueue(5))  # prints True
#    print(myQueue.enqueue(6))  # prints True
#    print(myQueue.enqueue(9))  # prints True
#    print(myQueue.enqueue(5))  # prints False
#    print(myQueue.enqueue(3))  # prints True
#    print(myQueue.size())  # prints 4
#    print(myQueue.dequeue())  # prints 5
#    print(myQueue.dequeue())  # prints 6
#    print(myQueue.dequeue())  # prints 9
#    print(myQueue.dequeue())  # prints 3
#    print(myQueue.size())  # prints 0
#    print(myQueue.dequeue())  # prints Queue Empty!


#if __name__ == "__main__":
#   Main()