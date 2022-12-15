class Solution:
    SYMBOL_MAP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    def romanToInt(self, s: str) -> int:
        res = 0

        cursor = 0
        while cursor < len(s):
            single_s = s[cursor]
            double_s = s[cursor : cursor + 2]

            if double_s in self.SYMBOL_MAP:
                res += self.SYMBOL_MAP[double_s]
                cursor += 2
            else:
                res += self.SYMBOL_MAP[single_s]
                cursor += 1

        return res
