# Recursion

*Recursion* is an approach to solving problems using a function that calls
itself as a subroutine.

The trick is that each time a recursive function calls itself, it reduces the
given problem into subproblems.  The recursion call continues until it reaches
a point where the subproblem can be solved wihtout further recursion.

Recursive functions should have these properties:
1. A simple `base case` (or `base cases`), identifying a terminating scenario
   that does not use recursion to produce an answer.
1. A set of rules, known as `recurrence relation` that reduces all other cases
   towards the `base case`.


## Recursion Function
For a problem, if there exists a recursive solution, we can follow the below
guidelines to implement it.

Suppose we want to implement some recursive function \\(F(X)\\)
1. Break the problem down into smaller scopes, such as \\(x_0 \in X, x_1 \in X, ..., x_n \in X\\)
1. Call function \\(F(x_0),F(x_1),...,F(x_n)\\) recursively to solve the
   subproblems of \\(X\\).
1. Finally, process the results form the recursive function calls to solve the
   problem corresponding to \\(X\\).


## Recurrence Relation
The *recurrence relation* is the relationship between the result of a problem
and the result of its subproblems.

The recursive call is performed according to the recurrence relation and it
should drive the function towards the `base case`.
