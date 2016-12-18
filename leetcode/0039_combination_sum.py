from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return get_combination(candidates, target)


def get_combination(
    candidates: List[int],
    target: int,
    current_sum: int = 0,
    current_combo: Optional[List[int]] = None,
) -> List[List[int]]:
    current_combo = current_combo or []
    if current_sum == target:
        return [current_combo]
    elif current_sum > target:
        return []

    results = []
    for i, candidate in enumerate(candidates):
        if candidate + current_sum > target:
            continue

        results.extend(
            get_combination(
                candidates[i:],
                target,
                current_sum + candidate,
                current_combo + [candidate],
            )
        )
    return results


assert len(Solution().combinationSum([2, 3, 5], 8)) == 3
assert len(Solution().combinationSum([2, 3, 6, 7], 7)) == 2
