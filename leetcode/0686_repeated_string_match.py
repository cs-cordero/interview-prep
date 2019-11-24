class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(A) > len(B):
            A, B = B, A

        start = B.find(A)
        if start == -1 or start > len(A):
            return -1

        i = start
        for j, character in enumerate(B):
            if character != A[i]:
                return -1
            i = (i + 1) % len(A)

        return (len(B) - 1) // len(A) + (start > 0)
