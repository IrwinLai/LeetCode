class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        d2 = d.copy()
        k = sorted(list(d.keys()))
        for i in range(len(k)):
            if i != 0:
                d[k[i]] += d[k[i-1]]
        ret = []
        for i in nums:
            ret.append(d[i] - d2[i])
        return ret