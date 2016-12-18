from typing import List, Optional, Set, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[Tuple[int]]:
        return list(get_combination(candidates, target))


def get_combination(
    candidates: List[int],
    target: int,
    current_sum: int = 0,
    current_combo: Optional[List[int]] = None,
) -> Set[Tuple[int]]:
    current_combo = current_combo or []
    if current_sum == target:
        return {tuple(sorted(current_combo))}
    elif current_sum > target:
        return set()

    results = set()
    for i, candidate in enumerate(candidates):
        if candidate + current_sum > target:
            continue

        results |= get_combination(
            candidates[i + 1 :],
            target,
            current_sum + candidate,
            current_combo + [candidate],
        )
    return results


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
