# Floyd-Warshall Algorithm

The *Floyd-Warshall (FW)* algorithm is an All-Pairs Shortest Path (APSP)
algorithm.  This means it can find the shortest path between _all pairs_ of
nodes.

The time complexity to run FW is \\(O(V^3)\\), which makes it ideal for graphs
*no larger than a couple hundred nodes*.

## Representation
The optimal way to represent the graph for the FW algorithm is with a 2D
adjacency matrix.

If there is no edge from node `i` to node `j`, then set the edge value for
`m[i][j]` to be positive infinity.

### Main idea
The main idea behind the Floyd-Warshall algorithm is to gradually build up all
intermediate routes between nodes i and j to find the optimal path.

In order to do so, we will need to use *dynamic programming*, through a 3D
matrix for a memo table.

## Algorithm Overview
1. `dp[k][i][j]` represents the shortest path from `i` to `j`, routing through
   nodes `{0,1,...,k-1,k}`
1. `dp[k][i][j] = m[i][j] if k == 0`
1. Otherwise:  `dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])`

### Space improvement
* Since you do not need earlier versions of `k` after reusing them once, you
  could just overwrite them in place with a 2D array.
* `dp[i][j] = m[i][j] if k == 0`
* Otherwise:  `dp[i][j] = min(dp[i][j], dp[i][j]+dp[k][j])`

## Pseudocode
```
n = size of the adjacency matrix
dp = the memo table that will contain APSP solutions
next = matrix used to construct shortest paths

function floydWarshall(m):
    setup(m)

    for (k := 0; k < n; k++):
        for (i := 0; i < n; i++):
            for (j := 0; j < n; j++):
                if dp[i][j] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][j] + dp[k][j]
                    next[i][j] = next[i][k]
    propagateNegativeCycles(dp, n)
    return dp
