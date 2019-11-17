# Network Flow

### Prerequisite
1. A *flow graph*, which is a directed graph with edges that have some
   specified *capacity* and which cannot be exceeded.
    * Edges also store a *flow value* which is the "units of flow" that is
      currently running through that edge.  This is expressed as
      `flow_value/capacity`.
    * Edges begin with 0 flow value until some max flow algorithm is run on it.
    * Flow graphs also have two types of special nodes on it, denoted `s` and
      `t`, which represent `sources` and `sinks`, respectively.  Flow flows
      from the sources infinitely to `t`, but are restricted by the edge
      capacities.

## A max flow algorithm: the Ford-Fulkerson method
* To find the maximum flow (and min-cut as a by-product), the Ford-Fulkerson
  method repeatedly finds *augmenting paths* through the *residual graph*, and
  *augments the flow* until no more augmenting paths can be found.
* An *augmenting path* is a path of edges in the residual graph with unused
  capacity greater than zero from the source `s` to the sink `t`.  It can only
  flow through paths that are not saturated yet.  You know that you have
  achieved max flow when there are no more augmenting paths remaining.
    *  In any augmenting path there is always some *bottleneck* value, which is
       the "smallest" edge on the path.  We can use that bottleneck value to
       *augment the flow* along the path.
    *  Bottleneck value = min(all _remaining_ capacities on edges along the path)
* *Augmenting the flow* means _updating_ the flow values of the edges along the
  augmenting path.  In other words, you increase the flow by the bottleneck
  value.
    *  When augmenting the flow along the augmenting path, you also need to
       *decrease the flow* along each residual edge by the same value.
* The *residual graph* is the flow graph that also contains residual edges,
  which have a flow/capacity of 0/0, but which support negative flow values.
  Each residual edge points backwards in the direction that the real edges
  point.

### Time Complexity of Ford-Fulkerson
It depends on what algorithm you use to find augmenting paths.

* *DFS*:  \\(O(fE)\\) where \\(f\\) is the maximum flow and \\(E\\) is the
  number of edges.
* *Edmonds-Karp*:  \\(O(E^2\*V)\\)
    * Uses a BFS as a method of finding augmenting paths.
* *Capacity scaling*:  \\(O(E^2log(U))\\)
    * Adds a heuristic on top of Ford-Fulkerson to pick larger paths first.
* *Dinic's algorithm*:  \\(O(V^2E)\\)
    * Uses a combination of BFS + DFS.
* *Push Relabel*:  \\(O(V^2E)\\) \\(O(V^2\sqrt{E})\\)
    * Uses a concept of maintaining a "preflow" instead of finding augmenting paths.
