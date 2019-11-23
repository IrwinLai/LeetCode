class Solution(object):
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = {};
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[len(nums)-1]
        

'''class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums) == 3:
            return max(nums[0]+nums[2],nums[1])
        
        else:
            sums = nums[:2]
            sums.append(max(nums[0]+nums[2],nums[1]))
            for i in range(3,len(nums)):
                sums.append(nums[i] + max(sums[i-2],sums[i-3]))
        return max(sums)
'''