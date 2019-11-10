from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket1_type = None
        basket1_count = 0
        basket2_type = None
        basket2_count = 0

        pointer1 = 0
        pointer2 = 0

        count = 0
        best_count = 0

        while pointer2 < len(tree):
            while pointer2 < len(tree):
                current_tree_type = tree[pointer2]
                if basket1_type is None or basket1_type == current_tree_type:
                    basket1_type = current_tree_type
                    basket1_count += 1
                elif basket2_type is None or basket2_type == current_tree_type:
                    basket2_type = current_tree_type
                    basket2_count += 1
                elif current_tree_type not in (basket1_type, basket2_type):
                    break

                pointer2 += 1
                count += 1
                best_count = max(best_count, count)

            while pointer2 < len(tree) and pointer1 < pointer2:
                lost_tree_type = tree[pointer1]
                if basket1_type == lost_tree_type:
                    basket1_count -= 1
                    if basket1_count == 0:
                        basket1_type = None
                else:
                    basket2_count -= 1
                    if basket2_count == 0:
                        basket2_type = None

                pointer1 += 1
                count -= 1

                if basket1_type is None or basket2_type is None:
                    break
        return best_count


print(Solution().totalFruit([1, 2, 1]))
print(Solution().totalFruit([0, 1, 2, 2]))
print(Solution().totalFruit([1, 2, 3, 2, 2]))
print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
