import numpy as np

class Deque:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start = -1
        self.end = 0
        self.num_el = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __deque_full(self):
        return (self.start == 0 and self.end == self.capacity - 1) or (self.start == self.end + 1)

    def _deque_empty(self):
        return self.start == -1

    def insert_start(self, value):
        if self.__deque_full():
            print("Deque is full")
            return

        if self.start == -1:
            self.start = 0
            self.end = 0
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.start -=1

        self.values[self.start] = value

    def insert_end(self, value):
        if self.__deque_full():
            print("Deque is full")
            return

        if self.start == -1:
            self.start = 0
            self.end = 0
        elif self.end == self.capacity - 1:
            self.end = 0
        else:
            self.end += 1

        self.values[self.end] = value

    def exclude_start(self):
        if self._deque_empty():
            print('Deque is empty')
            return

        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.start == self.capacity - 1:
            self.start = 0
        else:
            self.start += 1

    def exclude_end(self):
        if self._deque_empty():
            print('Deque is empty')
            return

        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.end == 0:
            self.end = self.capacity - 1
        else:
            self.end -= 1

    def get_start(self):
        if self._deque_empty():
            print('Deque is empty')
            return

        return self.values[self.start]

    def get_end(self):
        if self._deque_empty() or self.end < 0:
            print('Deque is empty')
            return

        return self.values[self.end]

    def print_self(self):
        print(self.values)


dq = Deque(5)

dq.insert_start(4)
dq.insert_start(9)
dq.insert_start(8)
dq.insert_start(7)
dq.insert_start(5)

dq.print_self()

print(dq.get_start())
print(dq.get_end())

dq.exclude_end()
dq.exclude_end()
dq.exclude_start()
print(dq.get_start())
print(dq.get_end())

dq.insert_end(5)
dq.print_self()
print(dq.get_start())
print(dq.get_end())