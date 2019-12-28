class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        m = max(list(d.values()))
        for i in list(d.keys()):
            if d[i] == m:
                return i