class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = sorted(candies)
        highest = temp[-1]
        result = []
        for i in candies:
            if i + extraCandies < highest:
                result += [False]
            else:
                result += [True]

        return result
