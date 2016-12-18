# Priority Queues

A *priority queue* is an Abstract Data Type that operates similar to a normal
queue except that _each element has a certain priority_.  The priority of the
elements in the priority queue determine the order in which elements are
removed from the Priority Queue.

By definition, priority queues only supports _comparable data_, meaning that
somehow, someway, the algorithms must know how to compare the priority of one
element from another and order them as higher/lower.

Priority queues are very closely related to *heaps*, but they are not strictly
so - they are an abstract data type.

## Example

```python
# Collection of element priorities (assorted):
priority_queue = <assorted collection: [14, 4, 8, 3, 1, 22]>  # pseudocode
priority_queue.poll()  # 1
priority_queue.add(2)
priority_queue.poll()  # 2
priority_queue.add(4)
priority_queue.poll()  # 3
priority_queue.add(5)
priority_queue.add(9)
priority_queue.poll()  # 4
priority_queue.poll()  # 4
priority_queue.poll()  # 5
priority_queue.poll()  # 8
priority_queue.poll()  # 9
priority_queue.poll()  # 14
priority_queue.poll()  # 22
```

### Heap
A *heap* is a tree-based data structure that satisfies some *heap invariant*,
(also called the *heap property*):  If A is a parent node of B then A is
ordered with respect to B for all nodes A, B in the heap.

You typically see max heaps or min heaps.

Heaps are used to maintain the priority queue specification.  It helps to
ensure that everytime `poll` is called, you get the next highest (or in the
example, the next lowest) priority.

### Priority queue uses:
1. Used in certain implementations of Dijkstra's Shortest Path algorithm.
1. Anytime you need to dynamically fetch the 'next best' or 'next worst' element.
1. Used in Huffman coding (which is often used for lossless data compression).
1. Best First Search (BFS) algorithms such as A\* use priority queues to
   continuously grab the next most promising node.
1. Used by Minimum Spanning Tree (MST) algorithms.


| Operation | Complexity |
|:---:|:---:|
|Binary Heap construction|\\(O(N)\\)|
|Polling|\\(O(log(N))\\)|
|Peek|\\(O(1)\\)|
|Inserting|\\(O(log(N))\\)|
|Naive Removing|\\(O(N)\\)|
|Advanced removing with Hash Table\*|\\(O(log(N))\\)|
|Naive contains|\\(O(N)\\)|
|Contains check with Hash Table\*|\\(O(1)\\)|

\* Using a hash table to help optimize these operations does take up linear
space and also adds some overhead to the binary heap implementation.

### Task: Transform a min-priority queue into a max-priority queue
* Method 1:  Negate the comparator such that A >= B becomes A <= B when polling.
* Method 2:  Negate the numbers as you insert them, then negate them again when
  they are taken out.

### Task: Adding Elements to Binary Heap
Priority queues are usually implemented with heaps since this gives them the
best possible time complexity.

There are many tiypes of heaps we could use to implement a priority, including:
* Binary Heap
* Fibonacci Heap
* Binomial Heap
* Pairing Heapo

A *binary heap* is a binary tree that also maintains the heap invariant.

A *complete binary tree* is a tree in which every level except possibly the
last is completely filled and all the nodes are as far left as possible.

Binary heaps can be represented under the hood as an array.
* This is convenient because insertions can just occur at the end.
* Let i be the parent node index
    * left child index == 2i + 1
    * right child index == 2i + 2

Insertion Instructions
1. Insert the new value at the end of the heap.
1. While the heap is in violation of the heap invariant, swap the new value
   with its parent.

### Task: Removing Elements from a Binary Heap
In general, you usually only want to `poll` the top of the heap.

Poll Instructions
1. Swap the root with the last node in the area
1. Free the root
1. Sink down the new root (which likely is violating the heap invariant).  To
   sink a node, compare it against its two children and swap with the lower (or
   higher) of the two.  In the case of a tie, use the left child.

If you want to `remove` a node, you would first have to search for it.

Remove Instructions
1. Start at the root
1. Perform a linear search to find the node you want to remove.
1. Swap the node with the last node in the tree.
1. Free the node.
1. Bubble up or bubble down (it could be either one regardless of whether it's
   a minheap or maxheap) the swapped node until the heap invariant is restored.

The inefficiency of the removal algorithm comes from the fact that we have to
perform a linear search to find out where an element is indexed at.  What if
instead we did a lookup using a hash table to find out where a node is indexed
at?
    * Q: But what if two nodes have the same value?  A: Maintain a mapping of
      the node value to a set of indexes.
    * Q: If we want to remove a node value that is repeated, does it matter
      which one we select?  A: No it does not, so long as after you remove it,
      the heap invariant is restored.

The optimized versions of the removal and insertion works the exact same,
except that whenever you need to search for a node or whenever nodes are
swapped, bubbled up, or sunk down, then the hashtable needs to also be updated.
