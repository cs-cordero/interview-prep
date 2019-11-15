class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def convert_to_isomorphic_representation(string: str) -> str:
            mapping = {}
            current = "a"
            representation = ""
            for character in string:
                mapped_character = mapping.get(character)
                if mapped_character:
                    representation += mapped_character
                    continue

                mapping[character] = current
                current = chr(ord(current) + 1)
            return representation

        return convert_to_isomorphic_representation(
            s
        ) == convert_to_isomorphic_representation(t)
