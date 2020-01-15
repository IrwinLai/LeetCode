import numpy as np
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        presum = [[0 for i in range(c+1)] for j in range(r+1)]
        res = [[0 for i in range(c)] for j in range(r)]
        
        for i in range(1,r+1):
            for j in range(1,c+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] + \
                            mat[i-1][j-1] - presum[i-1][j-1]
                
        for i in range(r):
            for j in range(c):
                a1 = min(i+K+1,r)
                a2 = min(j+K+1,c)
                b1 = max(0, i-K)
                b2 = max(0, j-K)
                res[i][j] = presum[a1][a2] + presum[b1][b2] - \
                        presum[a1][b2] - presum[b1][a2]
                print(a1,a2,b1,b2,res[i][j])
        print(presum)
                
        return res