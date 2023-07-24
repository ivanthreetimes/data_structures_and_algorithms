class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.

            new_node = Node(value)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            self.tail.head = new_node.value

    def __str__(self):
        current_node = self.head
        result = ''
        while current_node.next != None:
            result += str(current_node.value)
            current_node = current_node.next
        return result


linked_l = LinkedList()
linked_l.append(10)
linked_l.append(20)
linked_l.append(30)
linked_l.append(40)
linked_l.append(50)
print(linked_l)
