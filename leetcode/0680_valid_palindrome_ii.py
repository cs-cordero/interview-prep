class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(left: int, right: int, may_recurse: bool) -> bool:
            while left <= right:
                if s[left] != s[right]:
                    return may_recurse and (
                        helper(left + 1, right, False) or helper(left, right - 1, False)
                    )
                left += 1
                right -= 1
            return True

        return helper(0, len(s) - 1, True)
