class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        n = len(nums)
        for i in range(n):
            tem = nums[i]
            for j in range(i+1,n):
                if nums[j] > nums[j-1]:
                    tem += nums[j]
                else:
                    break
            ans = max(ans,tem)
        return ans