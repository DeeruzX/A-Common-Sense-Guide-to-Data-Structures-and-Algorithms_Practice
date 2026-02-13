#I have to review TreeNode

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

    def search(self, value, node):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self.search(value, node.leftChild)
        else:
            return self.search(value, node.rightChild)

    def insert(self, value, node):
        if value < node.value:
            if node.leftChild is None:
                node.leftChild = TreeNode(value)
            else:
                self.insert(value, node.leftChild)
        elif value > node.value:
            if node.rightChild is None:
                node.rightChild = TreeNode(value)
            else:
                self.insert(value, node.rightChild)

    def delete(self, valueToDelete, node):
        if node is None:
            return None
        elif valueToDelete < node.value:
            node.leftChild = self.delete(valueToDelete, node.leftChild)
            return node
        elif valueToDelete > node.value:
            node.rightChild = self.delete(valueToDelete, node.rightChild)
            return node
        elif valueToDelete == node.value:
            if node.leftChild is None:
                return node.rightChild
            elif node.rightChild is None:
                return node.leftChild
            else:
                node.rightChild = self.lift(node.rightChild, node)
                return node

    def lift(self, node, nodeToDelete):
        if node.leftChild:
            node.leftChild = self.lift(node.leftChild, nodeToDelete)
            return node
        else:
            nodeToDelete.value = node.value
            return node.rightChild

    def traverse_and_print(self, node):
        if node is None:
            return
        self.traverse_and_print(node.leftChild)
        print(node.value)
        self.traverse_and_print(node.rightChild)

    def display(self, node=None, level=0):
        if node is None:
            node = self
        if node.rightChild:
            self.display(node.rightChild, level + 1)
        print('    ' * level + str(node.value))
        if node.leftChild:
            self.display(node.leftChild, level + 1)


node_1 = TreeNode(10)
node_2 = TreeNode(20)
root = TreeNode(15, node_1, node_2)

node_1.leftChild = TreeNode(5)
node_1.rightChild = TreeNode(12)

node_2.leftChild = TreeNode(17)
node_2.rightChild = TreeNode(25)
root.traverse_and_print(root)
root.display()


