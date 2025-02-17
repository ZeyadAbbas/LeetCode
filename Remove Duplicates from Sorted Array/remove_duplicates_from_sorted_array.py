class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        count = 0
        for i, value in enumerate(nums):
            if value not in temp:
                temp.append(value)
                nums[count] = value
                count += 1

        return len(temp)
