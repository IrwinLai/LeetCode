class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        presum = 0
        count = {}
        count[0] = 1
        res = 0
        for i in A:
            presum += i
            res += count.get(presum%K,0)
            count[presum%K] = count.get(presum%K,0) + 1
        return res