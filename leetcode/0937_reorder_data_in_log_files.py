import string
from typing import List, Tuple


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, message = log.split(" ", 1)
            if message[0] in string.digits:
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        def letter_sort_key(log: str) -> Tuple[str, str]:
            identifier, message = log.split(" ", 1)
            return (message, identifier)

        return sorted(letter_logs, key=letter_sort_key) + digit_logs
