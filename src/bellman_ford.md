# Bellman-Ford Algorithm

The *Bellman-Ford (BF)* algorithm is a Single Source Shortest Path (SSSP)
algorithm.  This means it can find the shortest path from one node to any other
node.

It is _not_ ideal for most SSSP problems because it has a time complexity of
\\(O(E\*V)\\).  It is usually better to use Dijkstra's algorithm which is much
faster.  Dijkstra's is on the order of \\(O((E+V)log(V))\\) when using a binary
heap priority queue

## If Dijkstra's is better, then when should we use Bellman-Ford?
In short: use it when Dijkstra's is not appropriate.

For example, use it when the graph has negative edge weights.  This is when BF
is handy because it can be used to detect negative cycle and determine exactly
where they occur.

## Algorithm Overview
Let \\(E\\) be the number of edges.
Let \\(V\\) be the number of vertices.
Let \\(S\\) be the id of the starting node.
Let \\(D\\) be an array of size V that tracks the best distance from S to each node.

1.  Set every entry in D to `float("inf")`
1.  Set D[S] = 0
1.  Process and relax each edge V-1 times.  Basically the algorithm is just
    trying to minify the edges over and over again until it logically shouldn't
    get any lower (V-1 times to be sure).

```
for iteration in range(V-1):
    for edge in graph.edges:
        from, to, cost = edge
        if D[from] + cost < D[to]:
            D[to] = D[from] + cost
```

After completing the BF algorithm once, you can repeat the loop again... and
again for V-1 times, to identify all *negative cycles* in the graph.
```
for iteration in range(V-1):
    for edge in graph.edges:
        from, to, cost = edge
        if D[from] + cost < D[to]:
            # this "to" vertex is either part of the negative cycle or
            # reachable from the negative cycle, so we mark it with negative
            # infinity as a sentinel value.
            D[to] = float("-inf")  
```
