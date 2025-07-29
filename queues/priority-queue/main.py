import numpy as np

class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_el = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __empty_queue(self):
        return self.num_el == 0

    def __full_queue(self):
        return self.capacity == self.num_el

    def enqueue(self, value):
        if self.__full_queue():
            print("Queue is full")
            return

        if self.num_el == 0:
            self.values[self.num_el] = value
            self.num_el += 1
        else:
            x = self.num_el - 1
            while x >= 0:
                if value > self.values[x]:
                    self.values[x + 1] = self.values[x]
                else:
                    break
                x -= 1

            self.values[x + 1] = value
            self.num_el += 1


    def dequeue(self):
       if self.__empty_queue():
           print('Queue is empty')
           return

       valor = self.values[self.num_el - 1]
       self.num_el -= 1
       return valor

    def first(self):
        if self.__empty_queue():
            return -1
        return self.values[self.num_el -1]

q = PriorityQueue(5)

print(q.first())

q.enqueue(4)
q.enqueue(3)
q.enqueue(6)
q.enqueue(5)

print(q.first())

q.dequeue()

print(q.first())

q.dequeue()

print(q.first())
