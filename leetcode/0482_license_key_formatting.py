class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.upper().replace("-", "")
        last = len(S)
        countdown = K
        result = []
        for i in range(len(s) - 1, -1, -1):
            countdown -= 1
            if countdown == 0:
                result.append(s[i:last])
                last = i
                countdown = K
        if countdown != K:
            result.append(s[:last])
        return "-".join(reversed(result))
