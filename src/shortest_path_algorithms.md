# Shortest Path Algorithms

## Overview
| | BFS | Dijkstra | Bellman-Ford | Floyd-Warshall |
|:-:|:-:|:-:|:-:|:-:|
|Complexity|\\(O(V+E)\\)|\\(O((V+E)log(V))\\)|\\(O(V\*E)\\)|\\(O(V^3)\\)
|Recommended Graph Size|Large|Large/Medium|Medium/Small|Medium|
|Good for APSP?|Only works on unweighted graphs|Ok|Bad|Yes|
|Can detect negative cycles?|No|No|Yes|Yes|
|Shortest path (weighted)|Incorrect|Best algorithm|Works|Bad in general|
|Shortest path (unweighted)|Best algorithm|Ok|Bad|Bad in general|
