# Dynamic Programming

Dynamic Programming (DP) is an algorithmic technique for solving an
optimization problem by breaking it down into simpler subproblems and
utiliizing the fact that the optimal solution to the overall probelm depends
upon the optimal solution to its subproblems.

## Characteristics
1. Overlapping Subproblems
    * Subproblems are smaller versions of the original problem.  Any problem
      has overlapping sub-problems if finding its solution involves solving the
      same subproblem multiple times.

1. Optimal Substructure Property
    * Any problem has optimal substructure property if its overall optimal
      solution can be constructed from the optimal solutions of its
      subproblems.


> For example, to find `fib(4)`, you need to determine `fib(3)` and `fib(2)`.  To
> find `fib(3)`, you need to find `fib(2)` and `fib(1)`.  To find `fib(2)` you
> need to find `fib(1)` and `fib(0)`.  Finally, `fib(1)` and `fib(0)` are both
> constant knowns (the base cases).
>
> Fibonacci demonstrates the Overlapping Subproblems characteristic because
> `fib(2)`, `fib(1)` and `fib(0)` happen multiple times in different subproblem
> paths.
>
> Fibonacci demonstrates the Optimal Substructure Property because summing the
> results of the subproblems yields you the answer to the overall desired
> result, for `fib(4)`.

## Methods
Dynamic Programming offers two methods.

1. Top-down with Memoization
    * We try to solve the bigger problem by recursively finding the solution to
      smaller sub-problems.  When we solve a sub-problem, we cache its result so
      that we don't end up solving it repeatedly if it's called multiple times.
1. Bottom-up with Tabulation
    * We try to solve the bigger problem by solving all the related
      sub-problems first.  This is done typically by filling an n-dimensional
      table.  Based on the in-the-moment results in the table, the solution to
      the top/original problem is eventually computed.

> *On the naming of the methods*
> 
> "Top-down" refers to the fact that we attempt to solve the top problem first
> (which subsequently recurses down to solve the sub-problems).
> 
> In the "Bottom-up" version, we don't start with the top problem, we start
> with some known starting point and then build up to the top answer.
> Typically the answers in the n-dimensional table are incomplete until the
> final cell, which represents the answer for our top problem.

## Tips
* **Always start with a brute-force recursive solution**, which is the best way
  to start solving any DP problem.  Once you have a recursive solution, you can
  then apply memoization and tabulation techniques.


## Subtypes
### 0/1 Knapsack
### Unbounded Knapsack
### Fibonacci Numbers
### Palindromic Subsequences
* Recurse with two pointers at both ends, either reduce both sides towards the
  center, or try one side then the other.
* Sometimes you can create a 2D binary array that marks the start to ends that
  are palindromes, then use that to your advantage.

```python
def helper(start: int, end: int) -> ...:
    if s[start] == s[end]:
        # the ends match, so you can try
        # start to end is a palindrome if the longest substring inside is equal
        # to end - start - 1
        return helper(start+1, end-1)
    else:
        # the ends dont match so you have to try
        a = helper(start+1, end)
        b = helper(start, end-1)

        return max(a, b)
        # return 1 + min(a, b)  # can count deletions
```

### Longest Common Substring
* LCS (Longest Common Substring and Longest Common Subsequence)
* LIS (Longest Increasing Subsequence)
* LRS (Longest Repeating Subsequence)

### Bottom Up Equations
* `max(dp[i-1][j], prices[i] + dp[i][j-lengths[j]])`
* `dp[i-1][j] + dp[i][j-lengths[j]]`
* `min(dp[i-1][j], dp[i][j-value] + 1)`
