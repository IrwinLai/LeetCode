class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s = set(arr1) - set(arr2)
        d1 = collections.Counter(arr1)
        ret = []
        for i in arr2:
            ret.extend([i]*d1.get(i))
        for i in sorted(s):
            ret.extend([i]*d1.get(i))
        return ret