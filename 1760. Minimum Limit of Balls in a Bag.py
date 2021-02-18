class Solution:
    def minimumSize(self, nums: List[int], ma: int) -> int:
        def helper(n,k):
            if n % k == 0:
                return n//k - 1
            return n//k
            
        l,r = 1,max(nums)
        while l<r:
            m = l+(r-l)//2
            c = 0
            for num in nums:
                c += helper(num,m)
            #print(m,c)
            if c > ma:
                l = m+1
            else:
                r = m
            
        return r