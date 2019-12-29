class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_index = len(S) - 1
        t_index = len(T) - 1
        while True:
            if s_index < 0 and t_index < 0:
                return True
            elif S[s_index] == "#":
                backspace_count = 1
                s_index -= 1
                while s_index >= 0 and backspace_count > 0:
                    backspace_count += 1 if S[s_index] == "#" else -1
                    s_index -= 1
            elif T[t_index] == "#":
                backspace_count = 1
                t_index -= 1
                while t_index >= 0 and backspace_count > 0:
                    backspace_count += 1 if T[t_index] == "#" else -1
                    t_index -= 1
            elif s_index >= 0 and t_index >= 0:
                if S[s_index] != T[t_index]:
                    return False
                s_index -= 1
                t_index -= 1
            elif s_index < 0 or t_index < 0:
                return False


Solution().backspaceCompare("y#fo##f", "y#f#o##f")
Solution().backspaceCompare("ab##", "c#d#")
Solution().backspaceCompare("bxj##tw", "bxj###tw")
