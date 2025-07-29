import numpy as np

# -- UNORDERED ARRAYS

class UnorderedArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def print_self(self):
        if self.last_position == -1:
            print("Array is empty")
        else:
            for i in range(self.last_position +1):
                print(f'{i} - {self.values[i]}')

    # O(1) - O(2)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print("Max capacity reached")
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    # O(n)
    def search(self, value):
        for i in range(self.last_position + 1):
            if value == self.values[i]:
                return i
        return -1

    # O(n)
    def exclude(self, value):
        position = self.search(value)

        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1



arr = UnorderedArray(4)

arr.print_self()

print('-----------')

arr.insert(4)
arr.insert(3)
arr.insert(16)
arr.insert(8)
arr.insert(2)

arr.print_self()

print('-----------')

print(arr.search(8))
print(arr.search(5))

print('-----------')

arr.exclude(3)
arr.exclude(4)
arr.exclude(8)

arr.print_self()

print('-----------')
arr.insert(6)
arr.insert(1)

arr.print_self()