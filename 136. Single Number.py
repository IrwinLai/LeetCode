class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        for i in list(d.keys()):
            if d[i] % 2 == 1:
                return i