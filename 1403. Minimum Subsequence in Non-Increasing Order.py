class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(nums)
        nums.sort(reverse = 1)
        tem = 0
        for i in range(n):
            tem += nums[i]
            s -= nums[i]
            if tem > s:
                ans = nums[:i+1]
                break
                
        zero = ans.count(0)
        for i in range(zero):
            ans.remove(0)
            
        return ans