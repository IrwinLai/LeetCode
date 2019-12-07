class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d1 = collections.Counter(arr)
        d2 = collections.Counter(d1.values())
        return len(d1) == len(d2)