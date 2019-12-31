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

def two_pointers_template3(collection: List[Any], ...) -> ...:
    result = []
    swap_point1 = 0
    swap_point2 = len(collection) - 1
    i = 0
    while i <= swap_point2:
        if some condition:
            swap elements at collection[i] and collection[swap_point1]
            swap_point1 += 1
        elif another condition:
            swap elements at collection[i] and collection[swap_point2]
            swap_point2 -= 1
        else:
            i += 1
```


#### Side note when counting subarrays (combinatorics)
> _User willye wrote_:
>
> I was SO close to solving this via sliding window, but couldn't come up with
> `ans += right - left + 1....`
>
> For those who are confused, let's use the example nums = [10,5,2,6]:
>   * If we start at the 0th index, [**10**,5,2,6], the number of intervals is
>     obviously 1.
>   * If we move to the 1st index, the window is now [10,**5**,2,6]. The new
>     intervals created are [5] and [10,5], so we add 2.
>   * Now, expand the window to the 2nd index: [10,5,**2**,6]. The new intervals
>     are [2], [5,2], and [10,5,2], so we add 3.
>   * The pattern should be obvious by now; we add `right - left + 1` to the
>     output variable every loop!
>
> [Link to Leetcode Comment](https://leetcode.com/problems/subarray-product-less-than-k/solution/)

## Fast and Slow Pointer
### When it is useful
* Useful for dealing with cyclic LinkedList or arrays.

### Complexity
* *Time Complexity*:  \\(O(N)\\)
* *Space Complexity*:  \\(O(1)\\), _usually_, dependent on the actual implementation.

### Template
```python
def has_cycle(head: Node) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
        return True
    return False
```

## Merge Intervals
### When it is useful
* When handling intervals that may overlap
* When you need to either find overlapping intervals or merge intervals if they overlap

### Complexity
* *Time Complexity*:  \\(O(N * log(N))\\), _usually_, since you often will need to sort based on the start time.
* *Space Complexity*:  \\(O(1)\\), _usually_, dependent on the actual implementation.

### Template
```python
def merge_interval(intervals: List[Interval]) -> List[Interval]:
    merged = []
    if not intervals:
        return merged

    intervals.sort(key=lambda interval: interval.start)
    start, end = intervals[0]
    for interval in intervals[1:]:
        if interval.start >= end:
            start = min(start, interval.start)
            end = min(end, interval.end)
        else:
            merged.append([start, end])
            start = interval.start
            end = interval.end
    return merged
```

## Cyclic Sort
### When it is useful
* When dealing with an array contianing numbers within a given range.

### Complexity
* *Time Complexity*:  \\(O(N)\\)
* *Space Complexity*:  \\(O(1)\\), _usually_, dependent on the actual implementation.

### Template

