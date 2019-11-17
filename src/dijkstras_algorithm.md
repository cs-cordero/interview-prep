# Dijkstra's Algorithm

*Dijkstra's algorithm* is a Single Source Shortest Path (SSSP) algorithm for
graphs with *non-negative edge weights*.

Depending on how the algorithm is implemented and what data structures are
used, the time complexity is typically \\(O(E\*log(V))\\), which is competitive
against other shortest path algorithms.

### Prerequisite
*  All edge weights must be non-negative.  This constraint is imposed to ensure
   that once a node has been visited, its optimal distance cannot be improved.

## Algorithm Overview
1. Maintain a `dist` array where the distance to every node is positive
   infinity.  Mark the distance to the start node `s` to be 0.
1. Maintain a PQ of key-value pairs of (node_index, distance) pairs which tell
   you which node to visit next based on sorted min value.
1. Insert `(s, 0)` into the PQ and loop while PQ is not empty, pulling out the
   next most promising `(node_index, distance)` pair
1. Iterate over all edges outwards from the current node and relax each edge
   appending a new `(node_index, distance)` key-value pair to the PQ for every
   relaxation.

### Finding the optimal path
Using the above overview you can get the optimal distance, but getting the
optimal path will also be quite challenging.

1. In addition to the `dist` array, store a `prev` array.  The starting node's
   index should be filled with `None`.  Then as the min_costs you calculate
   override the values in the `dist` array, fill the same index in the `prev`
   array with the node that it is coming from.
1. Once you have completed the algorithm, you can start from the ending index,
   then use the `prev` array to weave through the previous nodes until you get
   a `None` value, which was the start.

### Eager Dijkstra's Algorithm
* As you calculate the min cost, if it overrides the value in the `dist` array,
  then a new pairing is added to the the heap.  The more times that a `dist`
  index gets updated, the more likely that you will end up over-storing the
  number of key-value pairs to check.
    * This is a decent trade-off, because heap insertions are \\(log(N)\\) but
      removing the old element from the heap is \\(O(N)\\).
* However a more optimized solution is to use an *Indexed Priority Queue* which
  allows you to _update_ entries in the heap efficiently.

### D-ary Heap optimization
* Yet another optimization:  When executing Dijkstra's algorithm, especially on
  dense graphs, there are a lot more updates, i.e., `decreaseKey` operations,
  to key-value pairs than there are `dequeue` operations.
* A *D-ary* heap is a heap variant in which each node has D children.  This
  speeds up `decreaseKey` operations at the expense of more costly removals.
* In general, the value of D should be `D = E/V` to balance removals against
  `decreaseKey` operations, improving Dijkstra's time complexity to
  \\(O(E\*log\_{E/V}(V))\\), which is much better for dense graphs.

### The state of the art
The current state of the art is the Fibonacci heap which gives improves the
time complexity to \\(O(E+Vlog(V))\\), which is stupid fast.

However, Fibonacci heaps are very difficult to implement and have a large
enough constant amortied overhead to make them impractical unless your graph is
quite large.
