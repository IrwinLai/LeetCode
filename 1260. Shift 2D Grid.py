import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m*n)
        if k == 0:
            k = m*n
        g = np.array(grid)
        g = g.flatten()
        g = np.insert(g,0,g[-k:])
        g = np.delete(g,range(len(g)-k,len(g)))
        g = g.reshape(m,n)
        
        return g