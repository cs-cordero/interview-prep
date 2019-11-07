# Hash Tables

A *hash table* is a data structure that provides a mapping from keys to values
using a technique called *hashing*.

Keys must be unique, but values can be repeated.  Hash tables have "key-value pairs."

The key-value pairs you place in a hash table can be of any type, not just
strings and numbers, but also objects.  However the keys need to be *hashable*.

## Hash functions

A *hash function* is a function that maps a key `x` to a whole number in a fixed range

Hash functions could collide, meaning that two different inputs generate the
same resulting hash value.

Hash functions _must_ be *deterministic*.  If `H(x)` produces `y`.  Then `x`
should ALWAYS product `y`.

Many programming language enforce that the keys used in a hash table must be
*immutable*.

## Handling hash collisions

### Separate Chaining
*Separate chaining* deals with hash collisions by maintainaing a data structure
(usually a linked list) to hold all the different vlaues which hashed to a
particular value)

Each position in the hash table array is a linked list.  When a hash collision
occurs, we append to the end of the linked list a node containing both the key
and the value.

On lookups, we first use the hash function to determine the array index to look
at.  Then we traverse the data structure held at that index for the key we are
looking for.

For removals, perform a lookup and just remove the node from the underlying
data structure.


### Open addressing
*Open addressing* deals with hash collissions by finding another place within
the hash table for the object to go by offsetting it from the position to which
it hashed to.

When using open addressing, the key-value pairs are stored in the table itself,
without an additional data structure.  Because of this, we care a great deal
about the size ofour hash table and how many elements are currently in the
table.

\\(Load\ Factor\ =\ \dfrac{Items\ in\ Table}{Size\ of\ Table}\\)

The O(1) constant time behavior attributed to hash tables assumes the load
factor is kept below a certain fixed value.  This means that once load factor>
threshold, we need to grow the table and rehash the elements.

When a hash collision occurs, we begin a *probing sequence*, which is a
separate probing function.  You can choose different types of probing functions:
1. Linear probing: \\(P(x) = ax + b\\), where a, b are constants
1. Quadratic probing: \\(P(x) = ax^2 + bx + c\\), where a, b, c are constants
1. Double hashing: \\(P(k, x) = x * H2(k)\\), where \\(H2(k)\\) is a secondary hash function

Basically, while the hash value is colliding, perform and continue to perform
the probing sequence function until you DON'T collide, and then insert the
key-value pair into the array.

#### Caveat about open addressing
Most randomly selected probing sequences modulo N will produce a cycle shorter
than the table size N.

This becomes problematic because it causes an infinite loop during the probing
sequence!

In general we don't handle this issue, instead we avoid it by restricting our
domain of probing functions to those which produce a cycle of exactly length N

| Operation | Average | Worst | 
|:---:|:---:|:---:|
|Insertion|\\(O(1)\\)|\\(O(N)\\)|
|Removal|\\(O(1)\\)|\\(O(N)\\)|
|Search|\\(O(1)\\)|\\(O(N)\\)|

The constant time behavior is only true if you have a good uniform hash function!
