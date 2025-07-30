class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None

    def show_node(self):
        print(self.value)


class DoublyLinkedLists:
    def __init__(self):
        self.first: Node | None = None
        self.last: Node | None = None

    def __is_empty(self):
        return self.first is None

    def insert_start(self, value):
        new = Node(value)

        if self.__is_empty():
            self.last = new
        else:
            self.first.prev = new
        new.next = self.first
        self.first = new

        print("Value inserted!")
        return value

    def insert_end(self, value):
        new = Node(value)

        if self.__is_empty():
            self.first = new
        else:
            self.last.next = new
            new.prev = self.last
        self.last = new

        print("Value inserted!")
        return value

    def exclude_start(self):
        if self.__is_empty():
            print('List is empty')
            return

        temp = self.first

        if self.first.next is None:
            self.last = None
        else:
            self.first.next.prev = None
        self.first = self.first.next

        return temp

    def exclude_end(self):
        if self.__is_empty():
            print('List is empty')
            return

        temp = self.last

        if self.last.prev is None:
            self.first = None
        else:
            self.last.prev.next = None
        self.last = self.last.prev

        return temp

    def exclude_el(self, value):
        if self.__is_empty():
            print('List is empty')
            return

        curr = self.first

        while curr is not None and curr.value != value:
            curr = curr.next

        if curr.prev is None:
            self.first = curr.next
        else:
            curr.prev.next = curr.next

        if curr.next is None:
            self.last = curr.prev
        else:
            curr.next.prev = curr.prev

        return curr

    def show_from_start(self):
        if self.__is_empty():
            print('List is empty')
            return

        print('\nShowing from start')
        curr: Node | None = self.first

        while curr is not None:
            curr.show_node()
            curr = curr.next

    def show_from_end(self):
        if self.__is_empty():
            print('List is empty')
            return

        print('\nShowing from end')
        curr: Node | None = self.last

        while curr is not None:
            curr.show_node()
            curr = curr.prev

d_ll = DoublyLinkedLists()

d_ll.insert_start(1)
d_ll.insert_start(2)
d_ll.insert_start(3)
d_ll.show_from_start()
d_ll.show_from_end()

d_ll.insert_end(0)
d_ll.insert_end(-1)
d_ll.show_from_start()
d_ll.show_from_end()

d_ll.exclude_start()
d_ll.exclude_end()
d_ll.show_from_start()
d_ll.show_from_end()

d_ll.exclude_el(1)
d_ll.show_from_start()
d_ll.show_from_end()