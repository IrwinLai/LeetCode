class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(A[0])):
            B = [j[i] for j in A]
        
            if B!= sorted(B):
                count +=1
        
        return count