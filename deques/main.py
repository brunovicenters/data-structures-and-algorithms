import numpy as np

class Deque:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start = -1
        self.finish = 0
        self.num_el = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __deque_full(self):
        return (self.start == 0 and self.finish == self.capacity - 1) or (self.start == self.finish + 1)

    def _deque_empty(self):
        return self.start == -1

    def insert_start(self, value):
        if self.__deque_full():
            print("Deque is full")
            return

        if self.start == -1:
            self.start = 0
            self.finish = 0
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.start -=1

        self.values[self.start] = value

    def insert_finish(self, value):
        if self.__deque_full():
            print("Deque is full")
            return

        if self.start == -1:
            self.start = 0
            self.finish = 0
        elif self.finish == self.capacity - 1:
            self.finish = 0
        else:
            self.finish += 1

        self.values[self.finish] = value

    def exclude_start(self):
        if self._deque_empty():
            print('Deque is empty')
            return

        if self.start == self.finish:
            self.start = -1
            self.finish = -1
        elif self.start == self.capacity - 1:
            self.start = 0
        else:
            self.start += 1

    def exclude_finish(self):
        if self._deque_empty():
            print('Deque is empty')
            return

        if self.start == self.finish:
            self.start = -1
            self.finish = -1
        elif self.finish == 0:
            self.finish = self.capacity - 1
        else:
            self.finish -= 1

    def get_start(self):
        if self._deque_empty():
            print('Deque is empty')
            return

        return self.values[self.start]

    def get_finish(self):
        if self._deque_empty() or self.finish < 0:
            print('Deque is empty')
            return

        return self.values[self.finish]

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
print(dq.get_finish())

dq.exclude_finish()
dq.exclude_finish()
dq.exclude_start()
print(dq.get_start())
print(dq.get_finish())

dq.insert_finish(5)
dq.print_self()
print(dq.get_start())
print(dq.get_finish())