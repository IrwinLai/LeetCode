class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def f(arr,start,n):
            if arr[start] == -1:
                return 0
            if arr[start] == 0:
                return 1 # find 0
            tem = arr[start]
            arr[start] = -1
            if start-tem >= 0 and start+tem < n:
                return max(f(arr,start-tem,n),f(arr,start+tem,n))
            elif start-tem >= 0:
                return f(arr,start-tem,n)
            elif start+tem < n:
                return f(arr,start+tem,n)
            return 0 # not find
        
        return f(arr,start,n) == 1