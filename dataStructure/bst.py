# Left < node < Right
# No Duplicate

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def bstInsert(root, node):
    if root == None:
        return node
    else:
        if node.value < root.value:
            root.left = bstInsert(root.left, node)
        elif node.value > root.value:
            root.right = bstInsert(root.right, node)
        else:
            return root
    return root

def bstSearch(root, value):
    if root == None:
        return None
    if root.value == value:
        return root
    elif root.value < value:
        return bstSearch(root.right, value)
    else:
        return bstSearch(root.left, value)

testTree = Node(8)
testTree = bstInsert(testTree, Node(10))
testTree = bstInsert(testTree, Node(3))
testTree = bstInsert(testTree, Node(1))
testTree = bstInsert(testTree, Node(6))
testTree = bstInsert(testTree, Node(9))
testTree = bstInsert(testTree, Node(3))

result = bstSearch(testTree, 3)
print(result)


