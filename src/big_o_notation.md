# Big O Notation

Big-O Notation gives an upper bound of the complexity in the *worst* case,
helping to quantify performance as the input size becomes *arbitrarily large*.

Big-O Notation is used to describe how *time* and *space* scales as the inputs
to your algorithm grow.

## Complexity

The complexities are ordered below from smallest (best) to largest (worst).

| Complexity | Representation |
|:---|:---:|
|Constant Time|\\(O(1)\\)|
|Logarithmic Time|\\(O(log(N))\\)|
|Linear Time|\\(O(N)\\)|
|Linearithmic Time|\\(O(Nlog(N))\\)|
|Quadric Time|\\(O(N^2)\\)|
|Cubic Time|\\(O(N^3)\\)|
|Exponential Time|\\(O(b^N), where\ b > 1\\)|
|Factorial Time|\\(O(N!)\\)|


## Properties
Because we only care about the worst case scenarios, when N approaches infinity, we get to have some special powers over representing Big-O Notation.

If you add a constant to infinity, then it's still infinity.

1. You may remove constant coefficients or constant values from the notation.
    * \\(O(N + c) = O(N)\\)
    * \\(O(c * N) = O(N), where\ c > 0\\)

1. You may use the biggest factor in place of the smaller ones
    * \\(O(N^3 + N^2 + N + c) = O(N^3)\\)


## Examples

1. Finding all subsets of a set: \\(O(2^N)\\)
1. Finding all permutations of a strings: \\(O(N!)\\)
1. Sorting using mergesort: \\(O(Nlog(N))\\)
1. Iterating over all cells in a matrix of size N by M: \\(O(N*M)\\)
