from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = Counter(magazine)

        for letter in ransomNote:
            if letter not in letter_count.keys():
                return False

            letter_count.subtract(letter)
            if letter_count[letter] < 0:
                return False

        return True
