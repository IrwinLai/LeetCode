class Solution:
    def checkStraightLine(self, A: List[List[int]]) -> bool:
        n = len(A)
        if n == 1:
            return True
        if (A[0][0] - A[1][0]) != 0:
            k = (A[0][1] - A[1][1])/(A[0][0] - A[1][0])
        else:
            # k = infinite
            t = A[0][0]
            for i in A:
                if i[0] != t:
                    return False
            return True
        b = A[0][1] - k*A[0][0]
        
        for i in A:
            if i[0]*k+b != i[1]:
                return False
        return True
                