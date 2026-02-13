class TreeNode:
    def __init__(self,val,left=None,right=None):
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


node_1 = TreeNode(10)
node_2 = TreeNode(20)
root = TreeNode(15, node_1, node_2)

