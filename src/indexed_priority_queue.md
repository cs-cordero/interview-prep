# Indexed Priority Queue

An *Indexed Priority Queue* is a traditional priority queue variant which o top
of the regular PQ operations supports _quick updates and deletions_ of
_key-value pairs_.

It is important to be able to dynamically update the priority value of certain
keys within the queue, which could re-order the queue.

### Tips:
Create a bidirectional mapping between your N keys and the domain [0, N) using
a bidirectional hash table.
    * This is because usually priority queues are implemented as heaps under
      the hood, which internally use arrays, so having a mapping to integer
      keys facilitate indexing.

### Indexed Priority Queue Interface

| Interface | Runtime | 
|:--:|:--:|
| delete(ki) | \\(O(log(N))\\) |
| valueOf(ki) | \\(O(1)\\) |
| contains(ki) | \\(O(1)\\) |
| peekMinKeyIndex() | \\(O(1)\\) |
| pollMinKeyIndex() | \\(O(log(N))\\) |
| peekMinValue() | \\(O(1)\\) |
| pollMinValue() | \\(O(log(N))\\) |
| insert(ki, value) | \\(O(log(N))\\) |
| update(ki, value) | \\(O(log(N))\\) |
| decreaseKey(ki, value) | \\(O(log(N))\\) |
| increaseKey(ki, value) | \\(O(log(N))\\) |


The IPQ stores the following:
1. The bidirectional mapping between N keys and N `ki`s
1. An array `vals` representing the values stored for each of the N `ki`s
1. An array of `pm`s (positional map) storing the Node number in the
   binary heap that a given `ki` element can be found.
1. An array of `im`s (inverse map) storing the `ki` for each index, where the
   Node number is the index.
