class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        nums = sorted(nums)
        for i in range(len(nums)/2):
            sums += min(nums[2*i],nums[2*i+1])
        return sums