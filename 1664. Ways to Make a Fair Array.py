class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd, even = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            odd[i] += odd[i-1]
            even[i] += even[i-1]
            if i % 2 == 0:
                even[i] += nums[i]
            else:
                odd[i] += nums[i]
                
        ans = 0
        for i in range(n):
            tem1 = even[i-1] + odd[n-1] - odd[i]
            tem2 = odd[i-1] + even[n-1] - even[i]
            ans += (tem1 == tem2)
        return ans