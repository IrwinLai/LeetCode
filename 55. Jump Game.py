class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0+nums[0]
        for i,n in enumerate(nums):
            if i > m:
                return False
            m = max(m,i+n)
            if m >= len(nums)-1:
                return True
        return True
            