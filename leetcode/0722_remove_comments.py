from collections import deque
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        source = deque(source)

        block_comment_mode = False
        block_comment_line = ""
        line = ""
        while source or line:
            if not line:
                line = source.popleft()
                continue

            if block_comment_mode is False:
                index_line_comment = line.find("//")
                index_block_comment = line.find("/*")
                if index_line_comment == -1 and index_block_comment == -1:
                    result.append(f"{block_comment_line}{line}")
                    block_comment_line = ""
                    line = ""
                    continue
                elif index_block_comment == -1 or (
                    index_line_comment >= 0 and index_line_comment < index_block_comment
                ):
                    line = f"{block_comment_line}{line[:index_line_comment]}"
                    if line:
                        result.append(line)
                    block_comment_line = ""
                    line = ""
                    continue
                else:
                    block_comment_mode = True
                    block_comment_line += line[:index_block_comment]
                    line = line[index_block_comment + 2 :]
            else:
                index_block_close = line.find("*/")
                if index_block_close == -1:
                    line = ""
                    continue
                block_comment_mode = False
                line = line[index_block_close + 2 :]
                if not line and block_comment_line:
                    result.append(block_comment_line)
                    block_comment_line = ""
        return result
