# Static and Dynamic Arrays

## Static Array
A *static array* is a fixed length container containing N elements which are
*indexable* from the range `[0, n-1]`.  Can also be written as `[0, N)`.

Static arrays are stored in contiguous blocks in memory.

## Dynamic Array
A *dynamic array* is a variable-length container exactly like a static array,
except that it can *grow* or *shrink* in size.  It supports inserts, appends,
and deletions.

### Dynamic Array Implementation
1. Use a static array (this is how Python handles it)
    1. Create a static array with initial capacity.
    1. Add elements to the underlying static array, keeping track of the number
       of elements.
    1. If adding another element will exceed capacity, then create a new static
       array with twice the capacity and copy the original elements into it.


### Array uses:
1. Storing and accessing sequential data.
1. Temporarily storing objects.
1. Used by IO routines as buffers.
1. Lookup tables and inverse lookup tables.
1. Can be used to return multiple values from a function.
1. Used in dynamic programming to cache answers to subproblems.
    * Classic examples are the "knapsack problem" or the "coin change problem".

### Complexities
| | Static Array | Dynamic Array |
|:---:|:---:|:---:|
|Access|\\(O(1)\\)|\\(O(1)\\)|
|Search|\\(O(N)\\)|\\(O(N)\\)|
|Insert|\\(N/A\\)|\\(O(N)\\)|
|Append|\\(N/A\\)|\\(O(1), amortized\\)|
|Delete|\\(N/A\\)|\\(O(N)\\)|

* Access is constant time because of indexing.
* Search is linear time because at worst you have to iterate over all N
  elements to find a specific element you are searching for.
* Insert is not applicable to static arrays, since the array cannot be resized.
  Insert is linear time for dynamic arrays because all indexes after the
  insertion index must be moved over by 1.
* Append is not applicable to static arrays, since the array cannot be resized.
  Append is constant time for dynamic arrays in an amortized fashion because
  although the resizing and copying of values to a new static array must occur
  if the array grows too large, this happens so little that in general we can
  assume appending will be constant.
* Delete is not applicable to static arrays, sinc ethe array cannot be resized.
  Delete is linear time for dynamic arrays, since all remaining indexes must be
  moved to fill in the void created by the deletion.
