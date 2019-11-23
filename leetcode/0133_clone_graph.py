class Node:
    # Provided by Leetcode
    ...


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        clone_map = {}

        def helper(node: "Node") -> "Node":
            if node in clone_map:
                return clone_map[node]

            clone_map[node] = Node(node.val, neighbors=[])
            clone_map[node].neighbors = [
                helper(neighbor) for neighbor in node.neighbors
            ]
            return clone_map[node]

        return helper(node)
