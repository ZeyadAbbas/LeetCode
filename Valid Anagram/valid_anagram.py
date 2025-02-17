class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False

        for s_letter, t_letter in zip(s, t):
            count_s[s_letter] = count_s[s_letter] + 1 if s_letter in count_s else 1
            count_t[t_letter] = count_t[t_letter] + 1 if t_letter in count_t else 1

        return count_s == count_t
