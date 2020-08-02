class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n-1):
            tem = [0]*(n-1-i)
            for j in range(i,n):
                if grid[j][i+1:] == tem:
                    count += j-i
                    grid.insert(0,grid.pop(j))
                    break
                if j == n-1:
                    return -1
        return count