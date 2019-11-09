# Divide and Conquer (D&C)

A *divide and conquer* algorithm works by _recursively_ breaking the problem
down into two or more subproblems of the same or related type, until these
subproblems become simple enough to be solved directly.  Then one combines the
results of the subproblems to form the final solution.

Three steps:
1.  **Divide**:  Divide the problem \\(S\\) into a set of subproblems:
    \\(\\{S_1, S_2, ..., S_n\\}\\) where \\(n \geq 2\\), i.e., there are usually more
    than one subproblem.
1.  **Conquer**:  Solve each subproblem recursively.
1.  **Combine**:  Combine the results of each subproblem.

The essential part of D&C is to figure out the `recurrence relationship`
between subproblems and the original problem, which informs how the divide and
the combine steps interact.

### Examples of D&C Algorithms
* Quick sort
* Merge sort
* Validating a binary search tree
