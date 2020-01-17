class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(l):
            dp = [0 for i in range(len(l))]
            dp[0],dp[1] = l[0],max(l[0],l[1])
            for i in range(2,len(l)):
                dp[i] = max(dp[i-2] + l[i], dp[i-1])
            return dp[-1]
        
        if len(nums) == 0:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        return max(f(nums[1:]),f(nums[:-1]))