class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None

    def show_node(self):
        print(self.value)

class LinkedList:
    def __init__(self):
        self.first: Node | None = None

    def __is_empty(self):
        return self.first is None

    def insert_start(self, value):
        new = Node(value)
        new.next = self.first
        self.first = new

    def exclude_start(self):
        if self.__is_empty():
            print('List is empty')
            return None

        temp = self.first
        self.first = self.first.next
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

lin_lis = LinkedList()

lin_lis.insert_start(3)
lin_lis.insert_start(2)
lin_lis.insert_start(8)

lin_lis.show()


print(lin_lis.exclude_start())
lin_lis.show()
print(lin_lis.first)
print(lin_lis.exclude_start())
print(lin_lis.exclude_start())
lin_lis.show()

print(lin_lis.exclude_start())


lin_lis.insert_start(3)
lin_lis.insert_start(2)
lin_lis.insert_start(8)
search = lin_lis.search(3)

if search is not None:
    print(f'Value found! {search.value}')
else:
    print(f'Value not found')

lin_lis.show()

lin_lis.exclude_el(2)
lin_lis.exclude_el(8)
lin_lis.show()
lin_lis.exclude_el(5)
