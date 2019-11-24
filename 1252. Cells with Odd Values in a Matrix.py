import numpy as np
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        m = np.zeros((n,m))
        for i in indices:
            m[i[0],:] += 1
            m[:,i[1]] += 1
        
        
        m = map(lambda x:x%2,m)
        return int(np.sum(m))
            
        