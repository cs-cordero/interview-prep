from typing import List


def triplet_sum_close_to_target(arr: List[int], target_sum: int) -> int:
    best = float("inf")
    best_dist = float("inf")
    arr.sort()

    for a in range(len(arr) - 2):
        b = a + 1
        c = len(arr) - 1
        target = target_sum - arr[a]
        while b < c:
            current_sum = arr[b] + arr[c]
            if current_sum == target:
                return target_sum

            actual_sum = current_sum + arr[a]
            actual_dist = abs(actual_sum - target_sum)
            if actual_dist < best_dist or (
                actual_dist == best_dist and actual_sum < best
            ):
                best = actual_sum
                best_dist = actual_dist

            if current_sum > target:
                c -= 1
            else:
                b += 1
    return best


triplet_sum_close_to_target([1, 0, 1, 1], 100)
