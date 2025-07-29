import numpy as np

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.num_el = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __empty_queue(self):
        return self.num_el == 0

    def __full_queue(self):
        return self.capacity == self.num_el

    def enqueue(self, value):
        if self.__full_queue():
            print("Queue is full!")
            return

        if self.end == self.capacity - 1:
            self.end = -1
        self.end += 1

        self.values[self.end] = value

        self.num_el += 1

    def dequeue(self):
        if self.__empty_queue():
            print("Queue is already empty!")
            return None

        temp = self.values[self.start]
        self.start += 1
        if self.start == self.capacity:
            self.start = 0
        self.num_el -= 1

        return temp

    def first(self):
        if self.__empty_queue():
            return -1
        return self.values[self.start]

q = Queue(4)


q.enqueue(2)
q.enqueue(6)
print(q.first())

q.enqueue(4)
q.enqueue(3)
print(q.first())

print(q.dequeue())
print(q.dequeue())
print(q.first())
