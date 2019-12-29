def backspace_compare(s: str, t: str) -> bool:
    s_index = len(s) - 1
    t_index = len(t) - 1
    while True:
        if s_index < 0 and t_index < 0:
            return True
        elif s[s_index] == "#":
            backspace_count = 1
            s_index -= 1
            while s_index >= 0 and backspace_count > 0:
                backspace_count += 1 if s[s_index] == "#" else -1
                s_index -= 1
        elif t[t_index] == "#":
            backspace_count = 1
            t_index -= 1
            while t_index >= 0 and backspace_count > 0:
                backspace_count += 1 if t[t_index] == "#" else -1
                t_index -= 1
        elif s_index >= 0 and t_index >= 0:
            if s[s_index] != t[t_index]:
                return False
            s_index -= 1
            t_index -= 1
        elif s_index < 0 or t_index < 0:
            return False
