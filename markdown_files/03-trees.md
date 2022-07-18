# **Data Structure 03: Trees**

* [Welcome](/markdown_files/00-welcome.md)
* [Queues](/markdown_files/01-queues.md)
* [Sets](/markdown_files/02-sets.md)
* [Trees](/markdown_files/03-trees.md)

---

## **Introduction**

In this project section, we will be studying the Tree data structure. Trees are hierarchical collections of elements called nodes that are linked together. The first node in a Tree is also known as the root node. All other nodes can be traced back to the root node since there are no unconnected nodes within a Tree data structure.

What is a node? A node is an element in a Tree that contains data and references to other nodes. In Figure 1, we can see different terms related to trees: Root, Parent Node, Child Node, Siblings, and more. These all represent a node.

<!-- Tree Chart -->
<figure>
<img src="https://scaler.com/topics/images/tree-data-structure-terminologies.webp">
<figcaption align = "center">Figure 1: Overview of Tree Data Structure Terms. <a href="https://www.scaler.com/topics/data-structures/tree-data-structure/">(Image Source)</a></figcaption>
</figure>

There are different types of Tree data structures. We will look at three of them: binary trees, binary search trees, and balanced binary search trees.

###### Binary Trees

A binary tree is a tree data structure that has at most two children nodes per node. In Figure 2, we can see that node 1 is the root. It has two children nodes, 7 and 9. We could keep following the tree nodes down and see that there are no nodes with more than two children nodes connected to it. 

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Binary_tree_v2.svg" style="height: 300px;">
<figcaption align = "left">Figure 2: Example Binary Tree. <a href="https://en.wikipedia.org/wiki/Binary_tree">(Image Source)</a></figcaption>
</figure>

###### Binary Search Trees

A binary search tree (BST) is essentially a Binary Tree; however, it follows different rules are procedures relating to the nodes within the tree. Data being added to a BST is compared to the parent nodes. If the data is smaller than the parent node, then it is added to the left. If it is larger, then it is added to the right. This ensures that the tree is sorted and organized. 

We can see this illustrated in Figure 3. Node 8 is the root node. 3 is less than 8, so it is added to the left. 10 is greater than 8, so it is added to the right. 

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Binary_search_tree.svg">
<figcaption align = "left">Figure 3: Example Binary Search Tree. <a href="https://en.wikipedia.org/wiki/Binary_search_tree">(Image Source)</a></figcaption>
</figure>

What if we want to add an element, but the root node already has two child nodes? If we wanted to add 20 to the BST in Figure 3, we would see that the root node is full so let's go down a level on the right. 20 is larger than 10, but there is already something in the right child node. Let's go down another level. 14 is now our parent node. 14 has a left child node 13, but there is nothing on the right of it! Since 20 is greater than 14 and node 14 has no right child node, we can add 20 there. 

As we can see, this results in a very efficient way to store and manipulate data. We did not have to view half of the elements in the tree to be able to add it. If this were any other data structure, this would most likely not be as efficient. 

###### Balanced Binary Search Trees

For a BST to perform efficiently, the tree must be balanced. In Figure 4, we can see an example of an unbalanced BST. With the root being 19 and each subsequent node being ordered in descending order, we are left with a one-sided tree. Compare this to the BST on the left. This tree is balanced just by changing the root node and rearranging some of the data. 

<figure>
<img src="https://stanford.edu/class/archive/cs/cs106b/cs106b.1158/images/balanced-tree-figure.png">
<figcaption align = "center">Figure 4: Example Balanced & Unbalanced Tree. <a href="https://stanford.edu/class/archive/cs/cs106b/cs106b.1158/preview-balanced-tree.shtml">(Image Source)</a></figcaption>
</figure>

A balanced tree is when the height between any two subtrees is not vastly different. Why is this necessary? It all comes down to performance. The unbalanced tree on the right in Figure 4 would perform many operations in O(n), while the balanced tree on the left would perform them in O(log n).

---

## **BST Operations & Big O**

Trees have multiple operations that allow us to manage the data in them. We will go over each of these operations for a BST and discuss their Big O performance below, but first we will build a BST class and a Node class nested in the BST class. The Node class will hold that data for the node. The BST class will contain all of the operations we can perform on a BST.

```python
class BST:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def __str__(self) -> str:
        # Return a representation of the tree.
        return str(list(self.traverse_forward()))
```

###### Insert O(log n)

Inserting a node into a BST occurs recursively. This is done by searching the subtrees for the next available and correct placement. This operations performs in an O(log n) time since we do not need to view all elements in the BST. Inserting a value into a BST can be accomplished in Python like this:

```python
def insert(self, data):
    if self.root is None:
        # The tree is empty, so we can just set the root to the new node.
        self.root = BST.Node(data)
    else:
        # There is already a root. 
        # Call _insert recursively to find the spot to insert.
        self._insert(data, self.root)

def _insert(self, data, node):
    if data < node.data:
        # The data belongs on the left side.
        if node.left is None:
            node.left = BST.Node(data)
        else:
            # Keep looking for the spot to insert.
            # Call _insert recursively on the left sub-tree.
            self._insert(data, node.left)
    elif data > node.data:
        # The data belongs on the right side.
        if node.right is None:
            node.right = BST.Node(data)
        else:
            # Keep looking for the spot to insert.
            # Call _insert recursively on the right sub-tree.
            self._insert(data, node.right)
    else:
        print("Duplicate node not inserted.")
```

###### Remove O(log n)

Removing a node from a BST also occurs recursively. This is done by searching the BST for the node, removing it's connections, and reconnecting each element that was disconnected so that we do not lose them unintentionally. This operations performs in an O(log n) time since we do not need to view all elements in the BST. Removing a value from a BST can be accomplished in Python like this:

```python
def delete(self, data):
    # Call the _delete function starting with the root node.
    self._delete(data, self.root)

def _delete(self, data, node):
    if node is None:
        print("Data not found.")
    elif data < node.data:
        self._delete(data, node.left)
    elif data > node.data:
        self._delete(data, node.right)
    else:
        # We found the node.
        if node.left is None and node.right is None:
            # The node has no children.
            node = None
        elif node.left is None:
            # The node has a right child only.
            node = node.right
        elif node.right is None:
            # The node has a left child only.
            node = node.left
        else:
            # The node has both children.
            # Find the smallest node in the right sub-tree.
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.data = temp.data
            self._delete(temp.data, node.right)
        print("Deleted node:", data)
```

###### Contains O(log n)

Checking a BST to see if a specific node is in it occurs recursively, again. To locate a value, we will search the BST and return a Boolean value on if the node is there or not. This operations performs in an O(log n) time since we do not need to view all elements in the BST. Checking the status of a value in a BST can be accomplished in Python like this:

```python
def contains(self, data):
    return self._contains(data, self.root)

def _contains(self, data, node):
    if node is None:
        return False
    elif data == node.data:
        return True
    elif data < node.data:
        return self._contains(data, node.left)
    elif data > node.data:
        return self._contains(data, node.right)
```

###### Traverse Forward O(n)

We can view all nodes in a BST from smallest to largest by recursively traversing the left subtrees and then the right subtrees. This can be done in Python like this:

```python
def traverse_forward(self):
    yield from self._traverse_forward(self.root)

def _traverse_forward(self, node):
    if node is not None:
        yield from self._traverse_forward(node.left)
        yield node.data
        yield from self._traverse_forward(node.right)
```

###### Traverse Backward O(n)

We can also view all nodes from largest to smallest by recursively traversing the right subtrees and then the left subtrees. This can be done in Python like this:

```python
def traverse_backward(self):
    yield from self._traverse_backward(self.root)

def _traverse_backward(self, node):
    if node is not None:
        yield from self._traverse_backward(node.right)
        yield node.data
        yield from self._traverse_backward(node.left)
```

###### Height O(n)

We can determine the height of a BST by starting at the root node and counting the maximum number of children in the tree. For example, in Figure 1, the height is 4. This is also done recursively and can be accomplished in Python like this:

```python
def get_height(self):
    return self._get_height(self.root)

def _get_height(self, node):
    if node is None:
        return 0
    else:
        return 1 + max(self._get_height(node.left), self._get_height(node.right))
```

###### Size O(1)

We can find how many nodes are in a BST by calculating how many nodes are in the tree. This is also done recursively and can be done in Python like this:

```python
def get_size(self):
    return self._get_size(self.root)

def _get_size(self, node):
    if node is None:
        return 0
    else:
        return 1 + self._get_size(node.left) + self._get_size(node.right)
```

###### Empty O(1)

To determine whether a BST is empty, we can use the size function or we can check to see if there is a root node. If there is no root node, then the tree is empty. This can be accomplished in Python like this:

```python
def is_empty(self):
        return self.root is None
```

---

## Coding example

Suppose we wanted to invert our binary tree. It seems that this is the infamous coding interview question. Well, let's take a look at it. Figure 5 illustrates what we will be trying to accomplish here. The tree on the right is inverted from the tree on the left.

<figure>
<img src="https://miro.medium.com/max/1250/0*gwBOA5wH-mwAWYMM.png">
<figcaption align = "center">Figure 5: Inverting a binary tree. <a href="https://medium.com/nerd-for-tech/binary-tree-coding-challenges-in-js-invert-a-binary-tree-and-number-of-islands-6c44e8718c22">(Image Source)</a></figcaption>
</figure>

Here is one way we can go about inverting our Binary Tree:

```python
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

def invert_tree(tree):
    if tree is None:
        return None

    # Swap the left and right subtrees.
    tree.left, tree.right = tree.right, tree.left

    # Recursively invert the subtrees.
    invert_tree(tree.left)
    invert_tree(tree.right)

    return tree
```

## Problem

Now it's your turn! Given a binary tree, write a function that returns the sum of all the node's integer values added together. You can download the [work file here](../python_files/BinaryTreeSum.py) and the [sample solution here](../python_files/solutions/BinaryTreeSumSolution.py). 