numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        last_value = 0

        for letter in s:
            value = numerals[letter]
            if last_value < value:
                total += value - (last_value * 2)
            else:
                total += value
            last_value = value

        return total
