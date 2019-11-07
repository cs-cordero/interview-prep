# Trees

A *tree* is an *undirected graph* which satisfies any of the following definitions:
1. An acyclic connected graph
1. A connected graph with N vertices and N-1 edges
1. A graph in which any two vertices are connected by _exactly one_ path.

A *rooted* tree is a tree with a "root node" that has no edges pointing
directly to it (aka it has no parent, or we say that its parent is itself), it
is the starting point for the tree.  We often want a reference to this root.
    * However, any node you pick can become teh root of its own sub-tree.

Terminology:
* Child node:  A node that extends from another node.
* Parent node:  The inverse of a child node.
* Leaf node:  A node that has no children.
* Subtree:  A tree entirely contained within another tree.


## Binary Tree

A *binary tree* is a tree for which every node has at most two child nodes.

## Binary Search Tree

A *binary search tree* is a binary tree that also satisfies the "binary search
tree invariant":  For all nodes, their left subtree has values less than the
node itself and the right subtree has values greater than the node itself.

### Binary Search Tree Uses:
1. Implementation of some map and set ADTs
1. Red Black Trees
1. AVL Trees
1. Splay Trees
1. Binary Heap implementations
1. Syntax trees
1. Treap - a probabilistic data structure

| Operation | Average | Worst | 
|:---:|:---:|:---:|
|Insert|\\(O(log(N))\\)|\\(O(N)\\)|
|Delete|\\(O(log(N))\\)|\\(O(N)\\)|
|Remove|\\(O(log(N))\\)|\\(O(N)\\)|
|Search|\\(O(log(N))\\)|\\(O(N)\\)|

### Operations

#### Insertion
1. Start at the root, move left or right based on the value of the node being inserted.
1. Once you hit empty, insert the node at that point!
1. One caveat -- if your BST supports duplicates, then decide which side the
   duplicate will belong to, and insert it there.  If it doesn't support
   duplicates, then do not insert.

#### Removal
1. Find the element you want to remove
1. Remove the element and replace it with its "successor" that would continue
   to support the BST invariant.
    * If the element is a leaf, then remove it with no side effects.
    * If the element has only one subtree, then the root of that subtree is the
      successor
    * If the element has two subtrees, then either the largest node in the left
      subtree or the smallest node in the right subtree is the successor.

#### Traversal
1. Preorder:  Explore the node as you visit it
1. Inorder:  Explore the node after visiting its entire left subtree
    1. Has the property of visiting all elements in sorted order.
1. Postorder: Explore the node after visiting both subtrees.
1. Level order traversal:  Print the nodes at each depth.
    1. This is performed through a breadth-first search (BFS), using a queue.
