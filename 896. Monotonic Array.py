class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        return A == sorted(A) or A == sorted(A, reverse = True)
        '''
        n = len(A)
        if A[-1] > A[0]:
            for i in range(1,n):
                if A[i-1] > A[i]:
                    return False
        else:
            for i in range(1,n):
                if A[i-1] < A[i]:
                    return False
        return True
        '''