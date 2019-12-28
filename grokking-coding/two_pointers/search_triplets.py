from typing import List


def search_triplets(arr: List[int]) -> List[List[int]]:
    triplets = set()
    for a in range(len(arr) - 2):
        for b in range(a + 1, len(arr) - 1):
            current_sum = arr[a] + arr[b]
            for c in range(b + 1, len(arr)):
                if current_sum + arr[c] == 0:
                    triplets.add(tuple(sorted([arr[a], arr[b], arr[c]])))
    return [list(triplet) for triplet in triplets]


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
