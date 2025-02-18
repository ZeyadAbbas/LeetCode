class Solution:
    def isValid(self, word: str) -> bool:
        consonant = "bcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"
        numbers = "1234567890"
        vowel_found = False
        consonant_found = False
        if len(word) >= 3:
            for char in word:
                if char not in numbers:
                    char = char.lower()
                    if char in vowels:
                        vowel_found = True
                    elif char in consonant:
                        consonant_found = True
                    else:
                        return False

            return vowel_found and consonant_found
        return False
