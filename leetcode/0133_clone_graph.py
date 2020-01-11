class Node:
    # Provided by Leetcode
    ...


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        original_to_clone_map = {}

        def helper(original: "Node") -> "Node":
            if original not in original_to_clone_map:
                original_to_clone_map[original] = Node(val=original.val, neighbors=[])
                original_to_clone_map[original].neighbors = [
                    helper(neighbor) for neighbor in original.neighbors
                ]
            return original_to_clone_map[original]

        return helper(node)
