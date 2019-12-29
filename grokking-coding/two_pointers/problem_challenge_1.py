from typing import List


def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:
    quadruplets = []
    if len(arr) < 4:
        return quadruplets

    arr.sort()
    a = 0
    while a < len(arr) - 3:
        b = a + 1
        while b < len(arr) - 2:
            c = b + 1
            d = len(arr) - 1
            while c < d:
                current = arr[a] + arr[b] + arr[c] + arr[d]
                if current == target:
                    quadruplets.append([arr[a], arr[b], arr[c], arr[d]])
                    c += 1
                    d -= 1
                    while c < d and arr[c] == arr[c - 1]:
                        c += 1
                    while c < d and arr[d] == arr[d + 1]:
                        d -= 1
                elif current > target:
                    d -= 1
                else:
                    c += 1
            b += 1
            while b < len(arr) - 2 and arr[b] == arr[b - 1]:
                b += 1
        a += 1
        while a < len(arr) - 3 and arr[a] == arr[a - 1]:
            a += 1

    return quadruplets


print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))
