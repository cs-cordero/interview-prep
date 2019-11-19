class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        letter_transforms = {}
        for source, target in zip(str1, str2):
            if letter_transforms.get(source) not in (None, target):
                return False
            letter_transforms[source] = target
        return len(set(letter_transforms.values())) < 26
