# Balanced Binary Search Trees & AVL Trees

A *Balanced Binary Search Tree* is a _self-balancing_ binary search tree.  This
type of tree will adjust itself in order to maintain a low (logarithmic)
height, allowing for faster operations such as insertions and deletions.

## BBST Complexities:

| Operation | Average | Worst | 
|:---:|:---:|:---:|
|Insert|\\(O(log(N))\\)|\\(O(log(N))\\)|
|Delete|\\(O(log(N))\\)|\\(O(log(N))\\)|
|Remove|\\(O(log(N))\\)|\\(O(log(N))\\)|
|Search|\\(O(log(N))\\)|\\(O(log(N))\\)|

### Tree Rotations
Central to all self-balancing trees is the concept of *tree rotations*.

The secret ingredient to most BBST algorithms is the clever usage of a _tree
invariant_ and _tree rotations_.

A *tree invariant* is a property/rule you impose on your tree that it must meet
after every operation.  To ensure that the invariant is always satisfied a
series of tree rotations are normally applied.

It might be weird that you are allowed to change the children of nodes in a BST
to how you see fit, but remember that it does not matter what the structure of
the tree looks like; all we care about is that the BST invariant holds.  This
means we can shuffle/transform/rotate the values and nodes in the tree as long
as the BST invariant remains satsified!

## AVL Tree

An *AVL tree* is one of the many types of BBSTs which allow for logarithmic
\((O(log(N))\\) insertion, deletion, and search operation.

In fact, it was the first type of BBST to be discovered.  Soon after, many
other types of BBSTs started to emerging, including the "2-3 tree", the "AA
tree", the "scapegoat tree", and its main rival, the "red-black tree".

### AVL Tree Invariant
The balanced factor (BF) is the AVL tree invariant!

\\(BF(node) = H(node.right) - H(node.left)\\)

where \\(H(x)\\) is the height of node x.  Recall that \\(H(x)\\) is calculated
as the number of edges between x and the furthest leaf.

The invariant in the AVL whcih forces it to remained balanced *is the
requirement that the balanced factor is always either -1, 0 or +1*.

We need to store the following information in each node:
1. The actual value we're storing in the node.  NOTE: This value msut be
   comparable so we know how to insert it.
1. A value storing this node's balance factor.
1. The height of this node in the tree.
1. Pointers to the left/right child nodes.

While the BF is not -1, 0, or +1, perform left or right tree rotations until it is.
