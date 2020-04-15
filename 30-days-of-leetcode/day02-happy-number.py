class Solution:
    def isHappy(self, n: int) -> bool:
        # Write an algorithm to determine if a number is "happy".
        #
        # A happy number is a number defined by the following process: Starting
        # with any positive integer, replace the number by the sum of the
        # squares of its digits, and repeat the process until the number equals
        # 1 (where it will stay), or it loops endlessly in a cycle which does
        # not include 1. Those numbers for which this process ends in 1 are
        # happy numbers.
        memo = {}

        def generate_next(num: int) -> int:
            if num not in memo:
                temp = num
                result = 0
                while temp:
                    result += (temp % 10) ** 2
                    temp //= 10
                memo[num] = result
            return memo[num]

        slow = n
        fast = generate_next(n)
        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                break
            slow = generate_next(slow)
            fast = generate_next(generate_next(fast))
        return fast == 1
