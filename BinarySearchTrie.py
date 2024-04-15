class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Construst the BST
r = Node(21)
r = insert(r, 14)
r = insert(r, 28)
r = insert(r, 11)
r = insert(r, 18)
r = insert(r, 15)
r = insert(r, 19)
r = insert(r, 25)
r = insert(r, 32)
r = insert(r, 30)

print("Inorder traversal of the constructed tree is")
inorder(r)