class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, treversal_type):
        if treversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif treversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif treversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Treversal type " + str(treversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        '''Root -> left ->  right'''
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, treversal):
        if start:
            treversal = self.inorder_print(start.left, treversal)
            treversal += (str(start.value) + '-')
            treversal = self.inorder_print(start.right, treversal)
        return treversal

    def postorder_print(self, start, treversal):
        if start:
            treversal = self.inorder_print(start.left, treversal)
            treversal = self.inorder_print(start.right, treversal)
            treversal += (str(start.value) + '-')
        return treversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right = Node(8)
#       1
#      / \
#     2   3
#    / \  /\
#   4   5 6 7

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))