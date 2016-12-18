from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        paragraphs = []
        i = 0
        while i < len(words):
            len_count_with_one_space = 0
            word_count = 0
            beginning_i = i
            while i < len(words):
                additional_len = len(words[i])
                if len_count_with_one_space + additional_len > maxWidth:
                    break
                len_count_with_one_space += additional_len + 1
                word_count += 1
                i += 1
            remaining_space = maxWidth - len_count_with_one_space + word_count

            if i == len(words):
                # last line
                line = " ".join(words[beginning_i:])
                padding = " " * (maxWidth - len(line))
                paragraphs.append(line + padding)
                break

            if word_count == 1:
                word = words[beginning_i]
                padding = " " * (maxWidth - len(word))
                paragraphs.append(word + padding)
                continue

            base_space_count = remaining_space // (word_count - 1)
            words_that_need_extra_space = remaining_space % (word_count - 1)

            left = words[beginning_i : beginning_i + words_that_need_extra_space]
            right = words[
                beginning_i + words_that_need_extra_space : beginning_i + word_count
            ]
            left_spacer = " " * (base_space_count + 1)
            right_spacer = " " * base_space_count
            intermediate = [
                group
                for group in [left_spacer.join(left), right_spacer.join(right)]
                if group
            ]
            line = left_spacer.join(intermediate)
            paragraphs.append(line)
        return paragraphs


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
result = Solution().fullJustify(words, maxWidth)
for row in result:
    print(f'"{row}"')

print()

words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
result = Solution().fullJustify(words, maxWidth)
for row in result:
    print(f'"{row}"')

print()

words = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
maxWidth = 20
result = Solution().fullJustify(words, maxWidth)
for row in result:
    print(f'"{row}"')
