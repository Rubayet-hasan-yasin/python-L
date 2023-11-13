# from Googler.DSA.linkedList import DoubleLinkedList
# from ..DSA.linkedList import DoubleLinkedList

class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size= 0


    def add(self, val):
        node = Node(val)

        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        
        self.size -= 1

    def remove_first(self):
        if self.head is not None:
            self.__remove_node(self.head)

    def remove_last(self):
        if self.tail is not None:
            self.__remove_node(self.tail)

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def front(self):
        return self.head.val
    
    def back(self):
        return self.tail.val

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return F"[{', '.join(str(val) for val in vals)}]"
    









class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def push(self, value):
        self.__list.add(value)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()
    
    def __len__(self):
        return self.__list.size
    

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.peek())
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
print(my_stack.pop())
print(len(my_stack))