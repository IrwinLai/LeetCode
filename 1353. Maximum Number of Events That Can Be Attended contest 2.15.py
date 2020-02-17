class Solution:
    def maxEvents(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:(x[0],x[1]))
        h = []
        res = d = 0
        
        while A or h:
            if not h:
                d = A[0][0]
            # push available item with nearest ddl
            while A and A[0][0] <= d:
                heapq.heappush(h,A.pop(0)[1])
            # pop not available item
            while h and h[0] < d:
                heapq.heappop(h)
            if h:
                heapq.heappop(h)
                res += 1
            d += 1
            
        return res