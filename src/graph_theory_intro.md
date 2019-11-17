# Graph Theory

*Graph theory* is the mathematical theory of the properties and applications of
graphs (networks).

## Types of Graphs
1. Undirected graph
    - A graph in which edges have no orientation.  Edge (U, V) is the same as
       edge (V, U).
1. Directed graph (digraph)
    - A graph in which edges do have orientation.  If there existed a directed
      edge from (U, V), it does not imply a corresponding opposite direction
      (V, U) unless the graph explictly has that edge.
1. Weighted graph
    - A graph with edges that contain certain "weight" to identify certain
      attributes or features.
1. Trees: An undirected graph with no cycles.
    1. Rooted tree
        -   A tree with a designated root node where all other nodes connect
            _to_ or connect _from_. If all nodes are pointing _towards_ the
            node, it is an in-tree.  Otherwise it is an out-tree.  Out-trees
            are significantly more common.
    1. Directed Acyclic Graph (DAGs)
        -   A directed graph with no cycles.
        -   All out-trees are DAGS, but not all DAGs are out-trees.
    1. Bipartite Graph
        -   A graph is one whose vertices can be split into two independent
            groups U, V such that every edge connects between U and V.
        -   Think assigning workers to bikes.
    1. Complete Graph
        -   A graph where there is a unique edge between every pair of nodes.

## Graph Representation
1. Adjacency Matrix (a 2D array)
    - `m[i][j]` represents the edge weight of going from node `i` to node `j`.
    - Pros:  Space efficient, edge weight lookup is \\((O(1)\)), very simple
      representation.
    - Cons:  Requires \\(O(V^2)\\) space.  Iterating over all edges takes
      \\(O(V^2)\\) time.
1. Adjacency List (a map of nodes to lists of edges.)
    - `m[i]` returns `List[Node]`.
    - Pros:  Space efficient for representing sparse graphs. Iterating over all
      edges is efficient.
    - Cons:  Less space efficient for denser graphs.  Edge weight lookup is
      \\(O(E)\\)  Slightly more complex graph representation.
1. Edge List (an unordered list of edges)
    - `m` is `List[Tuple[Node, Node, weight]]` so each element just identifies
      the edges.
    - This is seldomly used, but is practical in a handful of algorithms.
    - Pros:  Space efficient for sparse graphs. Iterating over edges is
      efficient.  Very simple structure.
    - Cons:  Less space efficient for denser graphs.  Edge weight lookup is \\(O(E)\\).


#### Ask yourself the following questions upon any graph problem:
1. Is the graph directed or undirected?
1. Are the edges of the graph weighted?
1. Is the graph likely to be sparse or dense with edges?
1. What representation should I use for the graph?

## Common Graph Theory Problems
1. Shortest path problem
    -   Given a weighted graph, find the shortest path of edges from node A to B.
    -   Algorithms:  BFS(unweighted), Dijkstra's, Bellman-Ford, Floyd-Warshall,
        A\*, etc.
1. Connectivity
    -   Does there exist a path between node A and node B?
    -   Algorithms:  Use union find data structure or any search algorithm, e.g., DFS.
1. Negative cycles
    -   Does my weighted digraph have any negative cycles?
    -   A negative cycle is one where the edges from A -> B -> C -> A have
        weights that add up to a negative number instead of 0.  Traveling
        through the cycle continually decreases the value of the weights to
        infinity.
    -   Algorithms:  Bellman-Ford and Floyd-Warshall
1. Strongly connected components
    -   A strongly connected component can be thought of as *self-contained
        cycles* within a *directed graph* where every vertex in a given cycle
        can reach every other vertex in the same cycle.
    -   Algorithms:  Tarjan's and Kosaraju's algorithm.
1. Traveling Salesman Problem
    -   Given a list of cities and the distances between each pair of cities,
        what is the shortest possible route that visits each city exactly once
        and returns to the origin city?
    -   This is NP-Hard, meaning it is a very computationally challenging
        problem.  This is unfortunate becasue this problem has very many
        important applications.
    -   Algorithms:  Held-Karp, branch and bound, and many approximation algorithms.
1. Bridges and Articulation Points
    -   Bridges are edges which, if removed, increases the number of connected
        components.
    -   Articulation points is any vertex in a graph whose removal increases
        the number of connected components.
    -   Connected component is like a block/group of connected nodes floating
        on its own.
1. Minimum Spanning Tree
    -   A minimum spanning tree (MST) is a subset of the edges of a connected,
        edge-weighted graph that connects all of the vertices together, without
        any cycles and with the minimum possible total edge weight.
    -   Algorithms:  Kruskal's, Prim's & Boruvka's algorithm.
1. Network flow: max flow
    -   With an infinite input source, how much "flow" can we push through the network?
    -   Suppose the edges of a graph are roads with cars, pipes with water, or
        hallways with people.  Flow represents the volume of water allowed to
        flow through the pipes, the number of cars the roads can sustain in
        traffic and the maximum amount of people that can navigate through the
        hallways.
    -   Algorithms:  Ford-Fulkerson, Edmonds-Karp & Dinic's algorithm.

## Traversal approaches
1. Depth-First Search (DFS) can be used to do the following:
    * Compute a graph's minimum spanning tree.
    * Detect and find cycles in a graph.
    * Check if a graph is bipartite.
    * Find strongly connected components.
    * Topologically sort the nodes of a graph.
    * Find bridges and articulation points.
    * Find augmenting paths in a flow network.
    * Generate mazes.
1. Breadth-First Search (BFS) is particularly useful for finding the shortest
   path on unweighted graphs.
