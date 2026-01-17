class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def print_linkedlist(self):
        current_node = self.first_node
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node.data
            current_node = current_node.next_node
            current_index += 1

        return None

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0

        while current_node is not None:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1
        return None

    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        current_node = self.first_node
        current_index = 0

        while current_node is not None:
            if current_index + 1 == index:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return
            current_node = current_node.next_node
            current_index += 1

    def delete_at_index(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        while current_node.next_node is not None:
            if current_index + 1 == index:
                current_node.next_node = current_node.next_node.next_node
                return
            current_node = current_node.next_node
            current_index += 1


# Build list
node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

data_set = LinkedList(node_1)

print(data_set.read(2))
print(data_set.index_of("time"))
data_set.delete_at_index(1)
data_set.print_linkedlist()
