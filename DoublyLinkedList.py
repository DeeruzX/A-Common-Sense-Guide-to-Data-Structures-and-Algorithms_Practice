# I will analze this code later, I'm sooo lazy today


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        new_node = Node(value)

        # If there are no elements yet in the linked list:
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enque(self, value):
        self.queue.insert_at_end(value)

    def deque(self):
        removed_node = self.queue.remove_from_front()
        return removed_node.data

    def tail(self):
        return self.queue.last_node.data
