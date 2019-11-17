# Basic DAG using Top Sort

### Prerequisite
1.  The graph must be a Directed Acyclic Graph

## Algorithm Overview
1. First get a topological sort.  As stated in those notes, this can be done in
   \\(O(V+E)\\) time.
1. For every node, store `float("inf")` as the total cost to reach each node.
1. Iterate through the topological ordering.  The very first node replaces its
   cost as 0 (as it doesn't cost anything to reach itself).
1. For each node, iterate over each of its edges, adding the weights of each
   edge to the current cost, then taking the min of that and its stored cost.
