import numpy as np

class Stack:

        def __init__(self, capacity):
            self.__capacity = capacity
            self.__top = -1
            self.__values = np.empty(self.__capacity, dtype=str)

        def __full_stack(self):
            if self.__top == self.__capacity - 1:
                return True
            else:
                return False

        def empty_stack(self):
            if self.__top == -1:
                return True
            else:
                return False

        def stack_up(self, value):
            if self.__full_stack():
                print("Stack is full")
            else:
                self.__top += 1
                self.__values[self.__top] = value

        def unstack(self):
            if self.empty_stack():
                print("Stack is empty")
            else:
                self.__top -= 1

        def top_item(self):
            if self.__top != -1:
                return self.__values[self.__top]
            else:
                return -1

        def print_self(self):
            for val in self.__values:
                print(val)


stc = Stack(20)

validate_char = {
    '{': '{',
    '}': '}',
    '[': '[',
    ']': ']',
    '(': '(',
    ')': ')',
}

closing_char = {
    ')': '(',
    '}': '{',
    ']': '[',
}

while True:

    inp = input("Type the next item of the expression:")
    if inp == "exit":
        break

    if len(inp) > 1:
        print('Invalid expression')
        continue

    if validate_char.get(inp):

        if closing_char.get(inp):
            if stc.top_item() == closing_char.get(inp):
                stc.unstack()
                continue
            else:
                print(f'Invalid expression, missing "{closing_char.get(inp)}"')
                break

        stc.stack_up(inp)


if stc.empty_stack():
    print("Valid expression!")
else:
    print("The are values that do not have pairs!")