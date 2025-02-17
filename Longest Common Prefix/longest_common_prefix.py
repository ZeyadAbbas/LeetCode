class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(prefix), -1, -1):
            for x, str in enumerate(strs):
                if prefix[0:i] not in str[0:i]:
                    break
                if x == len(strs) - 1:
                    return prefix[0:i]

        return ""
