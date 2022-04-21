class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.value),

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right  = Node(5)
root.left.left = Node(4)

printPostorder(root)