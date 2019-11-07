# Fenwick Trees (Binary Indexed Tree)

A *Fenwick Tree* (also called Binary Index Tree) is a data structure that
supports sum range queries as well as setting values in a static array and
getting the vlaue of the prefix sum up some index efficiently.

Note that the Fenwick tree's representation is a 1-based Array.  The index 0 is
unused.

## Motivation
Given an array of integer values, compute the range sum between index [i, j).
* You can do this in linear time, but you could do better.
* If the prefixed sums are already computed, you could compute ranges in O(1) time.
* But then what happens if you want to update the initial array with some new
  value?  The sums in the prefix sum array would need to be updated.


| Operation | Complexity |
|:---:|:---:|
|Construction|\\(O(N)\\)|
|Point Update|\\(O(log(N))\\)|
|Range Sum|\\(O(log(N))\\)|
|Range Update|\\(O(log(N))\\)|
|Adding Index|\\(N/A\\)|
|Removing Index|\\(N/A\\)|

### The Fenwick Tree
Unlike a regular array, in a Fenwick tree, a specific cell is responsible for
other cells as well.

The position of the *least significant bit* (LSB) of the array index in binary
form determines the range of responsibility that cell has to the cells below
itself.

```
16 10000  The LSB is in the 16th binary place, responsible for all 16 elements
15 01111  The LSB is in the 1th binary place, responsible for itself
14 01110  The LSB is in the 2th binary place, responsible for next 2
13 01101
12 01100  The LSB is in the 4th binary place, responsible for next 4
11 01011
10 01010
 9 01001
 8 01000  The LSB is in the 8th binary place, responsible for next 8
 7 00111
 6 00110
 5 00101
 4 00100
 3 00011
 2 00010
 1 00001
 0 00000
```

In a Fenwick tree, we may compute the *prefix sum* up to a certain index, which
ultimately lets us perform range sum queries.

Suppose you want to find the prefix sum of [1, i], then *you start at i and
cascade downwards* until you reach zero adding the value at each of the indices
you encounter.

For example:
Suppose you want to find the prefix sum of [1, 11):

\\(sum = A[11] + A[10] + A[8]\\)

A[11] is only responsible for itself.
A[10] is responsible for A[10] and A[9]
A[8] is responsible for A[8] through A[1], inclusive.

```
#!/usr/bin/pseudocode
function prefixSum(i):
    sum := 0
    while i != 0:
        sum = sum + tree[i]
        i = i - LSB(i)
    return sum

function rangeQuery(i, j):
    return prefixSum(j) - prefixSum(i-1)

function LSB(i):
   Returns the value of the least significant bit
```

### Point updates

Point updates are the opposite of traversing downward using the LSB.  With a
point update, we *add the LSB* to propagate the value up to the cells
responsible for given index i.

For example, if we add `x` to position `6` in the Fenwick tree, which cells do
we need to then modify?

```
we add the least significant bit to the number
 6 = 0110, 0110 + 0010 (the LSB) = 1000
 8 = 1000, 1000 + 1000 = 10000
16 = 10000, the boundary
```

Therefore the required updates are:
```
A[6] += x
A[8] += x
A[16] += x
```

or,

```
#!/usr/bin/pseudocode
function add(i, x):
    while i < N:
        tree[i] = tree[i] + x
        i = i + LSB(i)
```

### Construction

* Naive
    * Let A be an array of values. For each element in A at index i, perform a
      point update on the Fenwick tree with a vlaue of A[i].  There are n
      elements and each point update takes \\(O(log(N))\\) for a total of
      \\(O(N*log(N))\\).
* Linear
    * Add the value in the current cell to the *immediate cell* that is
      responsible for us.  This resembles what we did for point updates but
      only one cell at a time.
    * This will make the 'cascading' effect in range queries possible by
      propagating the value in each cell throughout the tree.
