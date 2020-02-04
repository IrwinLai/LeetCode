from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        @lru_cache(None)
        def helper(i):
            tem = 0
            for x in range(1,d+1):
                if i-x < 0 or arr[i] <= arr[i-x]:
                    break
                else:
                    tem = max(tem,helper(i-x))
                    
            for x in range(1,d+1):
                if i+x >= n or arr[i] <= arr[i+x]:
                    break
                else:
                    tem = max(tem,helper(i+x))
                    
            return tem+1
    
        return max(helper(i) for i in range(n))
