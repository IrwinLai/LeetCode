class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        count = 0
        tem = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                tem += 1
                count = max(tem,count)
            elif nums[i] != nums[i-1]:
                tem = 0
        return count+1