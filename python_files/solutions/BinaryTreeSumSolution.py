# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def sum_tree(tree):
    # If the tree is empty, return 0.
    if tree is None:
        return 0
    # If the tree is not empty, return the sum of the tree using recursion (check each node, right & left).
    return tree.node + sum_tree(tree.left) + sum_tree(tree.right)

# Test case 1:
bt = BinaryTree(1)
bt.left = BinaryTree(2)
bt.right = BinaryTree(3)
bt.left.left = BinaryTree(4)
bt.left.right = BinaryTree(5)
print(f'Binary Tree 1 Sum: {sum_tree(bt)}') # Should be 15.

# Test case 2:
bt2 = BinaryTree(10)
bt2.left = BinaryTree(20)
bt2.right = BinaryTree(30)
bt2.left.left = BinaryTree(40)
bt2.left.right = BinaryTree(50)
print(f'Binary Tree 2 Sum: {sum_tree(bt2)}') # Should be 150.

