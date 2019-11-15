import json
from typing import Any, Dict, Optional


class TreeNode:
    # Provided by Leetcode
    ...


class Codec:
    def serialize(self, root: TreeNode) -> str:
        def dict_creator(node: Optional[TreeNode]) -> Dict[str, Any]:
            if node is None:
                return None
            return {
                "value": node.val,
                "left": dict_creator(node.left),
                "right": dict_creator(node.right),
            }

        return json.dumps(dict_creator(root))

    def deserialize(self, data: str) -> TreeNode:
        def node_creator(data: Optional[Dict[str, Any]]) -> TreeNode:
            if data is None:
                return data

            node = TreeNode(data["value"])
            node.left = node_creator(data["left"])
            node.right = node_creator(data["right"])
            return node

        parsed_data = json.loads(data)
        return node_creator(parsed_data)
