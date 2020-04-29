class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        n = len(nums)
        h = []
        for i in range(n):
            for j in range(len(nums[i])):
                res.append([i+j,-i,nums[i][j]])
        res.sort()
        return [i[2] for i in res]
        '''
        res = []
        n = len(nums)
        h = []
        
        for i in range(n):
            for j in range(len(nums[i])):
                heapq.heappush(h, [i+j,-i,nums[i][j]])
                
        while h:
            res.append(heapq.heappop(h)[2])
        return res
        '''