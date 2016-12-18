from __future__ import annotations

from collections import deque
from typing import Any, Iterable, List, Optional


class _Empty:
    def __repr__(self) -> str:
        return "<Empty>"


Empty = _Empty()


class TreeNode:
    EMPTY = Empty

    def __init__(self, value: Any) -> None:
        self.val = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        return f"TreeNode({str(self.val)})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TreeNode) and self.val == other.val

    @classmethod
    def subtrees_match(cls, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a is None and b is None:
            return True

        return (
            isinstance(a, TreeNode)
            and isinstance(b, TreeNode)
            and a == b
            and cls.subtrees_match(a.left, b.left)
            and cls.subtrees_match(a.right, b.right)
        )

    @classmethod
    def from_array(
        cls, arr: List[Any], i: int = 0, allow_none: bool = False
    ) -> Optional[TreeNode]:
        """
        Usually makes sense to assume that values of None in an array mean no
        node should be created instead a TreeNode with value of None.
        If you want None to be converted to a TreeNode with value None, then
        set allow_none == True.
        """
        if (
            not arr
            or i >= len(arr)
            or arr[i] == cls.EMPTY
            or (allow_none and arr[i] is None)
        ):
            return None

        root = TreeNode(arr[i])
        root.left = cls.from_array(arr, i * 2 + 1)
        root.right = cls.from_array(arr, i * 2 + 2)
        return root

    def to_array(self) -> List[Any]:
        array = []
        queue = deque([self])
        while queue:
            node = queue.popleft()
            value = TreeNode.EMPTY if node is None else node.val
            array.append(value)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return array


def generate_permutations(base_list: List[Any]) -> Iterable[Any]:
    """
    Generates permutations in lexicographical order.
    1. Find highest j where arr[j] < arr[j+1]
    2. Find highest k where arr[j] < arr[k]
    3. Swap elements at indexes j and k
    4. Reverse in place all elements after the original j
    """
    if len(base_list) < 2:
        return None

    def find_index_j(arr: List[Any]) -> Optional[int]:
        j = None
        for i in range(len(arr) - 1):
            j = i if arr[i] < arr[i + 1] else j
        return j

    def find_index_k(arr: List[Any], k: int) -> int:
        k = k + 1
        for i in range(k, len(arr)):
            k = i if arr[i] > arr[k] else k
        return k

    copied_list = base_list[:]
    yield copied_list[:]
    while True:
        j = find_index_j(copied_list)
        if j is None:
            return None
        k = find_index_k(copied_list, j)
        copied_list[j], copied_list[k] = copied_list[k], copied_list[j]
        reverse_in_place(copied_list, left=j + 1)
        yield copied_list[:]


def quicksort_in_place(
    l: List[int], lower_bound: int = 0, upper_bound: int = None
) -> None:
    if upper_bound is None:
        upper_bound = len(l) - 1

    if lower_bound >= upper_bound:
        return

    pivot = l[upper_bound]
    target = lower_bound
    for i in range(lower_bound, upper_bound):
        if l[i] >= pivot:
            continue

        l[target], l[i] = l[i], l[target]
        target += 1
    l[upper_bound], l[target] = l[target], l[upper_bound]
    quicksort_in_place(l, lower_bound, target - 1)
    quicksort_in_place(l, target + 1, upper_bound)


def reverse_in_place(nums: List[int], left: int = 0, right: int = None) -> None:
    if not right:
        right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
