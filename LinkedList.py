class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while(second_last.next.next):
            second_last = second_last.next
        second_last.next = None

    def remove_from_beginning(self):
        if self.head:
            self.head = self.head.next

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        print(elements)

# Example usage:
ll = LinkedList()
ll.add_to_end(1)  # Add 1 to the end of the list
ll.add_to_beginning(2)  # Add 2 to the beginning of the list
ll.display()  # Display the list
ll.remove_from_end()  # Remove the last element from the list
ll.display()  # Display the list
ll.remove_from_beginning()  # Remove the first element from the list
ll.display()  # Display the list
