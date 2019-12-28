# Algorithms Overview

## Sliding Window
### When it is useful
* When dealing with a sequence and indexable collection (such as an array or
  LinkedList or string)
* You are asked to calculate something among all the _contiguous_ subarrays or
  sublists or substrings.

### Complexity
* *Time Complexity*:  \\(O(N)\\)
* *Space Complexity*:  \\(O(N)\\), _usually_, dependent on the actual implementation.

### Template
```python
def sliding_window_template(collection: List[Any], ...) -> ...:
    results = []
    hashmap = {}                        # a hashmap is often used to keep track of some
                                        # condition, state, or value within the window
    begin = 0                           # the beginning index of the sliding window
    for end in range(len(collection)):  # the ending index of the sliding window
        while some condition is not met:
            remove the element at collection[begin] to hashmap
            begin += 1                  # move the sliding window forward

        add the element at collection[end] to hashmap
        if some condition is met:
            manipulate the result set
    return result
```


## Two Pointers
### When it is useful
* When dealing with sorted arrays or with linked lists
* You are asked to find a set of elements that fulfill certain constraints
* The set of elements need not be contiguous.
* The set of elements could be a pair, a triplet, or even a subarray.

### Complexity
* *Time Complexity*:  \\(O(N)\\)
* *Space Complexity*:  \\(O(1)\\), _usually_, dependent on the actual implementation.

### Template
```python
def two_pointers_template(collection: List[Any], ...) -> ...:
    left = 0                     # initialize left pointer to first index
    right = len(collection) - 1  # initialize right pointer to last index

    while left < right:          # could also be <=
        if some condition is met:
            return some value
        if another condition that leverages the array being sorted:
            left += 1
        else:
            right -= 1
    return default or sentinel value

def two_pointers_template2(collection: List[Any], ...) -> ...:
    results = []
    left = 0        

    for right in range(len(collection)):
        if some condition is met:
            swap elements at collection[left] and collection[right]
            left += 1
    return left
```


## ...
### When it is useful
### Complexity
### Template
