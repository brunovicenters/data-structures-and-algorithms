import numpy as np

# -- Ordered Array

class OrderedArray:
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

        print("---------")

    # - O(n)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('Max capacity reached')
            return

        position = 0

        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break

            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x+1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1

    # O(n)
    def linear_search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] == value:
                return i
            if self.values[i] > value or self.last_position == i:
                return -1

    def binary_search(self, value):
        bot_pointer, top_pointer = 0, self.last_position

        if self.values[0] > value or self.values[self.last_position] < value:
            return -1

        while True:
            curr_position = int((top_pointer + bot_pointer) / 2)

            if self.values[curr_position] == value:
                return curr_position
            elif bot_pointer > top_pointer:
                return -1
            else:
                if self.values[curr_position] < value:
                    bot_pointer = curr_position + 1
                else:
                    top_pointer = curr_position - 1

    # O(n)
    def exclude(self, value):
        position = self.linear_search(value)

        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1

arr = OrderedArray(10)

arr.print_self()

arr.insert(8)
arr.print_self()

arr.insert(10)
arr.print_self()

arr.insert(4)
arr.insert(16)
arr.insert(6)

arr.print_self()

print(arr.linear_search(8))

print(arr.linear_search(6))

print(arr.linear_search(11))

print(arr.linear_search(16))

print(arr.linear_search(17))

print("-----------")

arr.exclude(6)
arr.exclude(16)
arr.exclude(4)
arr.print_self()

sec_arr = OrderedArray(10)
sec_arr.insert(8)
sec_arr.insert(2)
sec_arr.insert(3)
sec_arr.insert(5)
sec_arr.insert(7)
sec_arr.insert(12)
sec_arr.insert(4)
sec_arr.insert(6)

sec_arr.print_self()

print(sec_arr.binary_search(13))