class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        output = []
        for i in nums:
            output.append(sorted_nums.index(i))

        return output
