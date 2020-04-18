class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = 100
        for i in range(n):
            count += nums[i]
            res = min(res,count)

        return max(-res+1,1)
        