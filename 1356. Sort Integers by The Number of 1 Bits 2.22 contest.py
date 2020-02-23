class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x:(list(bin(x)[2:]).count('1'),x))
        return arr