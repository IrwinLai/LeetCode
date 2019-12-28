class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ret = [[] for i in range(len(A[0]))]
        for r in range(len(A)):
            for c in range(len(A[0])):
                ret[c].append(A[r][c])
        return ret