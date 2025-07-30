class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None

    def show_node(self):
        print(self.value)

class LinkedListWithTwoPointers:
    def __init__(self):
        self.first: Node | None = None
        self.last: Node | None = None

    def __is_empty(self):
        return self.first is None

    def insert_start(self, value):
        new = Node(value)
        new.next = self.first

        if self.__is_empty():
            self.last = new

        self.first = new

    def insert_end(self, value):
        new = Node(value)

        if self.__is_empty():
            self.first = new
        else:
            self.last.next = new
        self.last = new

    def exclude_start(self):
        if self.__is_empty():
            print('List is empty')
            return None

        temp = self.first
        self.first = self.first.next
        if self.__is_empty():
            self.last = self.first
        return temp

    def show(self):
        if self.__is_empty():
            print('List is empty')
            return

        curr: Node | None = self.first

        while curr is not None:
            curr.show_node()
            curr = curr.next

    def search(self, value):
        if self.__is_empty():
            print('List is empty')
            return None

        curr: Node = self.first

        while curr is not None and curr.value != value:
            curr = curr.next

        return curr

    def exclude_el(self, value):
        if self.__is_empty():
            print('List is empty')
            return None

        curr = self.first
        prev = self.first

        while curr is not None and curr.value != value:
            prev = curr
            curr = curr.next

        if curr is None:
            print(f"Value is not in the list! Value -> {value}")
            return None

        if value == self.first.value:
            self.first = curr.next
        else:
            prev.next = curr.next

        print(f'Succesfully exclude {curr.value}')
        return curr.value

ll_wp = LinkedListWithTwoPointers()
ll_wp.insert_end(0)
ll_wp.insert_start(3)
ll_wp.insert_start(4)
ll_wp.insert_start(5)
ll_wp.show()

ll_wp.insert_end(2)
ll_wp.insert_end(1)
ll_wp.show()

print('\nlast value:')
print(ll_wp.last.value)

print('\nexcluding items:')
ll_wp.exclude_start()
ll_wp.exclude_start()
ll_wp.exclude_start()
ll_wp.exclude_start()
ll_wp.exclude_start()
ll_wp.exclude_start()
ll_wp.show()
