# like robber2, pick up n//3 number in a list which can not contiguous and maximum the sumation
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        memo = {}
        size = len(slices)
        def dp(n, i, j): #n: need to choose n pizza, i: start index, j: end index (both included)
            if (n,i,j) in memo:
                return memo[(n,i,j)]
            if n == 0:
                return 0     
            if j - i + 1 < 2 * n - 1: #strong prunning1 : it's impossible to choose n pizza from slices[i:j+1]
                return -float('inf')       
            else:
                res_arr = []
                mx = -float('inf')
                for k in range(i,j+1):
                    if slices[k] > mx:
                        res_arr.append(slices[k] + dp(n-1,k+2,j))
                        mx = slices[k] # strong pruning 2, pick pre_arr max
                res = max(res_arr)
                memo[(n,i,j)] = res
                return res
                
        return max(dp(size // 3, 1, size-1), dp(size // 3, 0, size-2))