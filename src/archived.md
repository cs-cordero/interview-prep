# Technical Interview Notes

### Reading Material:
- [TSiege's Technical Interview Cheat Sheet](https://gist.github.com/cs-cordero/db0026f64aefac966b330db3db99de89)
- [Cracking the Coding Interview](http://www.barnesandnoble.com/p/cracking-the-coding-interview-gayle-laakmann-mcdowell/1122334602/2675519022102?st=PLA&sid=BNB_DRS_Marketplace+Shopping+Books_00000000&2sid=Google_&sourceId=PLGoP3840&k_clickid=3x3840)


### Absolute, Must-Have Knowledge:

| Data Structures       | Algorithms           | Concepts                |
| --------------------- | -------------------- | ----------------------- |
| Linked Lists          | Breadth-First Search | Bit Manipulation        |
| Trees, Tries & Graphs | Depth-First Search   | Memory (Stack vs. Heap) |
| Stacks & Queues       | Binary Search        | Recursion               |
| Heaps                 | Merge Sort           | Dynamic Programming     |
| Vectors / ArrayLists  | Quick Sort           | Big O Time & Space      |
| Hash Tables           |                      |                         |


## Arrays and Strings
1.  **Topics:**
    -   Sizing
        -   In more statically typed languages, you have to worry about the size of an array.
        -   In its most basic implementation, arrays store data sequentially with **fixed** space.  If you want to use an array that can be resized, you must implement a solution to allow it to grow in size.
        -   The most common resizing method is to create a new array with double the size of the first array, then copy the elements of the first array to the new array.
        -   In Python, lists are implemented as resizeable arrays, so thankfully, you do not have to worry about this.
    -   Optimization
        -   If an array is sorted, you can think about doing optimized search methods, like with a binary search.

2.  **Big O efficiency:**
    -   Indexing: O(1)
    -   Search: O(n)
    -   Insertion: O(n)
    -   Optimized Search: O(log n)


#### Sub-Topic: Hash Tables / Maps
1.  **Topics:**
    -   Hashing
        -   A hash table is a structure that stores arbitrary data.  In Python, sets are a hash table.  It need not be a storage of key-value pairs.
        -   A hash map is a hash table, but with a collection of key-value pairs.
        -   The relationship between a pair is based on a hash function.
        -   When you provide a hash table with a new key, a hash function takes the key and generates a hash value.
        -   The data structure underlying a hash table/map need not be thought of as an array.  You could implement the back-end of a hash table to be a balanced binary search tree, and the hash value result from the hash algorithm would point you to where in the tree your value is.  A BST hash table would have O(logN) lookup, but would potentially use less space.

    -   Collisions
        -   Two distinct pieces of data have the same hash value
        -   Put more simply, if you have two keys, 'a' and 'b' and in the hash map, the hash algorithm generates the exact same hash value, we have a collision.
        -   To handle collisions, two common ways would be to run the hash algorithm on the result recursively until you reach an unused hash value. Other ways would be to look around from the collision to find a new hash value.
        -   If the number of collisions is very high, the worst case runtime to retrieve an element starts to approach O(N).

2.  **Big O efficiency:**
    -   Indexing: O(1)
    -   Search: O(1)
    -   Insertion: O(1)

#### Array and String Methods:
1.  **isUnique()**
    -   Determine if a string or list has all unique elements. Attempt to do so without any additional data structures.
2.  **checkPermutation()**
    -   Given two strings, determine if one is a permutation of the other.
3.  **URLify()**
    -   Write a method to replace all spaces in a string with '%20'. Trim any spaces on the end.
4.  **palindromePermutation()**
    -   Given one string, determine if it is a permutation of a palindrome.
5.  **oneAway()**
    -   There are three possible edits to a string: insert a character, remove a character, or replace a character.  Given two strings, write a function to check whether they are one edit or zero edits away.
6.  **stringCompression()**
    -   Implement a method to perform basic string compression using the counts of repeated characters, i.e. 'aabcccccaaa' --> 'a2b1c5a3'
7.  **rotateMatrix()**
    -   Given a 2D array of NxN size, rotate the array 90 degrees **in place**.
8.  **zeroMatrix()**
    -   Given a 2D array of MxN size, if an element is 0, its entire row and column are set to 0.
9.  **stringRotation()**
    -   Assume you have a method isSubstring() which checks if one word is a substring of another.  Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring().


## Linked Lists

1.  **Topics:**
    -   Basic Implementation of a Linked List Node

            class Node(object):
                def __init__(self):
                    self.next = None
                    self.data = None


    -   Types of Linked Lists
        -   Singly Linked List
            -   Nodes are referenced in one direction.
        -   Doubly Linked List
            -   Nodes include pointers in the opposite direction.
        -   Circularly Linked List
            -   A linked list with a tail that references another node in the linked list, often the head.

2.  **Big O efficiency:**
    -   Indexing: O(n)
    -   Search: O(n)
    -   Insertion: O(1)
    -   Optimized Search: O(n)

#### Linked List Methods:
1.  **Insertion**
2.  **Deletion**
3.  **The "Runner" Technique**
    -   Iterating through the linked list with two pointers simultaneously, with one ahead of the other, i.e., have pointer 1 hop from one node to the next, but pointer 2 hops every other node.
4.  **removeDups()**
    -   Implement a function that removes duplicates from an unsorted linked list, without a temporary buffer.
5.  **return_kth_to_last()**
    -   Implement an algorithm to find the kth to last algorithm
6.  **deletefromMiddle()**
    -   Implement an algorithm to delete a node in the middle, i.e., any node but the first or last node, of a singly linked list, **given only access to that node.**
7.  **partition()**
    -   Implement an algorithm to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
8.  **sumLists()**
    -   Given two numbers represented as linked lists, where each node is a single digit, and where the digits are stored in reverse order, such that the 1's digit is at the ehad of the list, write a function that add sthe two numbers and returns the sum as a linked list.
    -   Suppose the digits are stored in forward order, repeat the above problem.
9.  **palindrome()**
    -   Given a linked list, implement an algorithm to determine if the linked list is a palindrome.
10. **intersection()**
    -   Given two singly linked lists, determine if the two lists intersect.  Return the intersecting node.  Intersection is defined based on reference, not value.  That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
11. **detectLoop()**
    -   Given a circular linked list, implement an algorithm that return sthe node at the beginning of the loop.


## Stacks and Queues

1.  **Topics:**
    -   Stacks
        -   Stacks are a data structure that supports LIFO ordering, i.e., the last item to be pushed onto the stack is the first item to be popped from it -- think like a stack of plates.
        -   In Python, the easiest implementation of a stack is to just use a list, since the pop() and append() functions already operate at O(1) time complexity.
    -   Queues
        -   Queues are a data structure that suppoers FIFO ordering, i.e., the first item to be pushed onto the queue is the first item to be popped from it -- think like a line at the movie theatre or a line to to ride a rollercoaster: the first person in line gets to go first.
        -   In Python, the best implementation of a queue is to import from the collections module the data type of `deque`, or a 'double-ended queue.'  Under the hood, a `deque` is implemented using a doubly linked list, and popping elements from the left is much more efficient.  A list is less efficient, because a queue requires you to append on one side of the list but pop from the other, and popping or appending on the left side of a list/array has O(n) time complexity.
    -   Constant time access
        -   The key to having a good stack or queue for its purpose is to have O(1) time access to the 'top' of the stack or the 'front' of the queue.
    -   Use cases
        -   Stacks are often useful in recursive algorithms.  Sometimes you need to push temporary data onto a stack as you recurse, then pop them as you backtrack.
        -   Queues are used in breadth-first search or in implementing a cache.

2.  **Big O efficiency:**
    -   Indexing: O(n)
    -   Search: O(n)
    -   Insertion: O(1)
    -   Push: O(1)
    -   Pop: O(1)

#### Stack and Queue Methods:
1.  **pop()**
2.  **push(item)**
3.  **peek()**
4.  **isEmpty()**
5.  **threeInOne()**
    -   Design a single array to implement three stacks.
6.  **stack_min()**
    -   Design a stack which, in addition to push and pop, has a function min which returns the minimum element.  Push, pop, and min should operate at O(1
7.  **stack_of_plates()**
    -   Implement a data structure `SetOfStacks` that mimics the creation of a new stack when a previous stack exceeds some threshold.  SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack.
    -   Implement a function popAt which performs a pop on a specific sub-stack.
8.  **queue_stacks()**
    -   Implement a MyQueue class which implements a queue using two stacks.
9.  **sort_stack()**
    -   Implement an algorithm to sort a stack such that the smallest items are on the top.  You can use an additional temporary stack, but no other data structure, e.g., array, etc.  Stacks support push, pop, peek, and isEmpty.
10. **animalshelter()**
    -   Animal shelter operates on a FIFO basis.  People must adopt either the oldest of all animals at the shelter.  They can select whether they want a dog or a cat, but they will get the oldest of that species.  Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.


## Trees and Graphs

1.  **Topics:**
    -   Basic Implementation of a Tree

            class Node(object):
                def __init__(self):
                    self.data = None
                    self.children = []
                    # or if binary tree:
                    self.left = None
                    self.right = None


    -   Types of Trees
        -   At a basic level, a tree is a data structure composed of nodes.  Each tree has a root node. Each node has zero or more child nodes.  Each child node has zero or more child nodes.  Each child node has a parent node.
        -   Trees may not contain cycles.  They don't have to be organized in any order and children may point back to their own parent nodes, but a node's child cannot be one of its ancestor nodes.
        -   A node is a 'leaf' it has no children.
        -   Binary Trees
            -   Binary trees are trees in which eahc node has up to two children.
        -   Binary Search Trees
            -   Binary search trees are binary trees where every node fits a specific ordering property: `all left descendents <= n < all right descendents, for all node n`.
        -   **Min-Heaps and Max-Heaps**
            -   Heaps are typically complete binary trees in which each node is smaller/larger than its children.
            -   Heaps allow for O(log n) insertion and extraction of the min element.
        -   Tries (aka Prefix Tree)
            -   "A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent a word."  Words terminate with a '*' node, also known as a 'null node.'
    -   Balance
        -   Balanced trees represent a concept for how lop-sided a tree is.  If the majority of the nodes extend from the right of the root, for example, then the tree is typically described as not balanced.
        -   Balancing a tree does not necessarily mean that the left and right subtrees are exactly the same size.  Ask your interviewer for clarification.
        -   Oftentimes "balanced" just means that it can ensure O(log n) for `insert` and `find`.
        -   Check out `red-black trees` and `AVL trees`.
    -   Completeness
        -   Complete binary trees are binary trees in which every level of the tree is filled except the right-most nodes on the last level.
    -   Full Binary Trees
        -   A full binary tree is a binary tree in which every node has either zero or two children.  No nodes have a single child.
    -   Perfect Binary Trees
        -   A binary tree that is both full and complete.  These are pretty rare in interviews and in real life, and never assume that a given tree is indeed perfect.

2.  **Big O efficiency:**
    -   Indexing: O(log n)
    -   Search: O(log n)
    -   Insertion: O(log n)

#### Sub-Topic: Graphs
1.  **Topics:**
    -   **Types of Graphs**
        -   Trees are technically a type of graph, but not all graphs are trees.  Trees are connected graphs without cycles.
        -   Graphs are a collection of nodes with edges between some or none of them.  Graphs may consist of multiple isolated subgraphs.
    -   Graph Direction
        -   Graphs can be directed or undirected.  Directed graphs mean that one node points to a second node only in one direction.  Undirected nodes mean that two nodes are connected in both directions.
    -   Implementation
        -   Graphs can be implemented in its own **class** that stores a list of its nodes.  Each node in turn stores its direction to other nodes (their children)
        -   Graphs can also be implemented in an **Adjacency List** or an **Adjacency Matrix**.  An adjacency list is basically a hash table where the keys are the nodes and the values are a list of their children.  An adjacency matrix is an NxN boolean matrix, where a true value indicates an edge from node i to node j.

2.  **Big O efficiency:**
    -   Indexing: N/A
    -   Search: O(n)
    -   Insertion: O(1)

#### Trees and Graphs Methods:
1.  **route_between_nodes()**
    -   Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
2.  **minimal_tree()**
    -   Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
3.  **list_of_depths()**
    -   Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists)
4.  **check_balanced()**
    -   Implement a function to check if a binary tree is balanced.  For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
5.  **validate_BST()**
    -   Implement a function to check if a binary tree is a binary search tree.
6.  **successor()**
    -   Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in a binary search tree.  You may assume taht each node has a link to its parent.
    -   How would you implement a solution if there is no link to its parent.
7.  **build_order()**
    -   You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project).  All of a project's dependencies must be built before the project is.  Find a build order that will allow the projects to be built.  If there is no valid build order, return an error.
    -   i.e.  input:
        -   projects: a, b, c, d, e, f
        -   dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
    -   output:
        -   f, e, a, b, d, c
8.  **first_common_ancestor()**
    -   Design an algorthm and write code to find the first common ancestor of two nodes in a binary tree.  Avoid storing additional nodes in a data structure.
9.  **BST_Sequences()**
    -   A binary search tree was created by traversing through an array from left to right and inserting each element.  Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
10. **check_subtree()**
    -   T1 and T2 are very large binary treees, with T1 much bigger than T2.  Create an algorithm to determine if T2 is a subtree of T1.  A tree T2 is a subtree of T1 if there exists a node in T1 that the subtree of n is identical to T2.
11. **random_node()**
    -   Implement a binary tree class from scratch which in addition to `insert`, `find`, and `delete`, has a method `getRandomNode()` which returns a random node from teh tree.  All nodes should be equally likely to be chosen.  Design and implement an algorithm for `getRandomNode()` and explain how you would implement the rest of the methods.
12. **paths_with_sum()**
    -   You are given a binary tree in which each node contains an integer value (which might be positive or negative).  Design an algorithm to count the number of paths that sum to a given value.  The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
