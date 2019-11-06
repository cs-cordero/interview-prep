# Disjoint Set (Union Find)

A *disjoint set*, also known as the *union find*, is a data structure that
keeps track of elements which ar split into one or more disjoint sets.  It has
two primary operations: *find* and *union*

### Disjoint set uses:
1. Kruskal's minimum spanning tree algorithm
1. Grid percolation
1. Network connectivity
1. Least commmon ancestor in trees
1. Image processing

| Operation | Complexity |
|:---:|:---:|
|Construction|\\(O(N)\\)|
|Union|\\(\alpha(N)\\)|
|Find|\\(\alpha(N)\\)|
|Get component size|\\(\alpha(N)\\)|
|Check if connected|\\(\alpha(N)\\)|
|Count components|\\(O(1)\\)|

* Where \\(\alpha\\) is amortized constant time

### Creating a Disjoint Set

1. Construct a _bijection_ (a one-to-one mapping) between your objects and the
   integers [0, n).  This mapping can be done arbitrarily.  You can store this
   bijection in a mapping.
    * Not strictly necessary, but this makes it easy to work with.
1. Construct an array.  Each index has an associated object.  This is kind of
   the bijection above but in the reverse direction.
