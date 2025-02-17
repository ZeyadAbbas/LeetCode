class Solution:
    def isValid(self, s: str) -> bool:
        left_brackets = {"(": 1, "[": 2, "{": 3}
        right_brackets = {")": 1, "]": 2, "}": 3}
        temp = ""

        if len(s) % 2 != 0:
            return False

        for i, bracket in enumerate(s):
            if bracket in right_brackets:
                if (
                    temp == ""
                    or right_brackets[bracket] != left_brackets[temp[len(temp) - 1]]
                ):
                    return False
                temp = temp[0 : len(temp) - 1]
            else:
                temp += bracket

            if i == len(s) - 1 and bracket in left_brackets:
                return False

        if temp == "":
            return True
        else:
            return False
