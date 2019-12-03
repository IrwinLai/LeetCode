class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        count[0] = 1 
        s = 0
        n = 0
        # presum of a is s, then find number of presum is s-k, their sumation is k
        for i in nums:
            s += i
            n += count.get(s-k,0)
            count[s] = count.get(s,0) + 1
        return n