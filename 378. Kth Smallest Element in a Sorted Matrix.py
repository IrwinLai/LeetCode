class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        ret = []
        for row in matrix:
            ret += row
        ret.sort()
        
        return ret[k-1]