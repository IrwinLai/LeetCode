class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        ans = 0
        for i in d:
            ans += d[i]*(d[i]-1)//2
        return ans