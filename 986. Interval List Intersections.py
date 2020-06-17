class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # double linked list
        ret = []
        i,j = 0,0
        while i < len(A) and j < len(B):
            if A[i][0] <= B[j][1] and A[i][1] >= B[j][0]:
                ret.append([max(A[i][0],B[j][0]),min(A[i][1],B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ret
                    