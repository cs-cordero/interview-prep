# Topological Sort

A *topological ordering* is an ordering of the nodes in a directed graph where
for each directed edge from node A to node B, node A appears before node B in
the ordering.

The topological sort algorithm cna find a topological ordering in \\(O(V+E)\\) time!

Many real world situations can be modeled as a graph with directed edges where
some events must occur before others.
* School class prerequisites
* Program dependencies
* Event scheduling
* Assembly instructions

## Algorithm
1. Pick an unvisited node
1. Perform DFS, exploring only unvisited nodes.
1. On the recursive callback, add the current node to the topological ordering
   in reverse order.

### Notes
* Topological orderings are NOT unique
* Only DAGs can generate a topological sort.
