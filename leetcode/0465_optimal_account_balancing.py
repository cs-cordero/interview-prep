from collections import defaultdict, deque
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        ledger = defaultdict(int)
        for source, target, amount in transactions:
            ledger[source] -= amount
            ledger[target] += amount

        balances = deque([balance for balance in ledger.values() if balance])
        result = 0
        while balances:
            queue = deque([(balances[0], [0], list(range(1, len(balances))))])
            while queue:
                amount, path, indexes = queue.popleft()
                if amount == 0:
                    for used_index in sorted(path, reverse=True):
                        balances.remove(balances[used_index])
                    result += len(path) - 1
                    break

                for remaining_index in indexes:
                    remaining_amount = amount + balances[remaining_index]
                    new_path = path + [remaining_index]
                    remaining_indexes = [j for j in indexes if j != remaining_index]
                    queue.append((remaining_amount, new_path, remaining_indexes))
        return result


print(Solution().minTransfers([[0, 1, 10], [2, 0, 5]]))
print(Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))
print(Solution().minTransfers([[1, 5, 8], [8, 9, 8], [2, 3, 9], [4, 3, 1]]))
print(
    Solution().minTransfers(
        [[10, 11, 6], [12, 13, 7], [14, 15, 2], [14, 16, 2], [14, 17, 2], [14, 18, 2]]
    )
)
print(Solution().minTransfers([[0, 1, 5], [0, 2, 5], [3, 4, 5], [3, 5, 5]]))
print(Solution().minTransfers([[1, 2, 3], [1, 3, 3], [6, 4, 1], [5, 4, 4]]))
print(Solution().minTransfers([[0, 3, 2], [1, 4, 3], [2, 3, 2], [2, 4, 2]]))
