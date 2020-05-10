from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ret = []
        if len(nums1)*len(nums2) > 0:
            heap = []
            heappush(heap, (nums1[0] + nums2[0], 0, 0))
            visit = [(0,0)]
            while len(ret) < k and heap:
                tem = heappop(heap)
                ret.append([nums1[tem[1]],nums2[tem[2]]])
                if tem[1]+1 < len(nums1) and (tem[1]+1,tem[2]) not in visit:
                    heappush(heap, (nums1[tem[1]+1] + nums2[tem[2]], tem[1]+1, tem[2]))
                    visit.append((tem[1]+1,tem[2]))
                if tem[2]+1 < len(nums2) and (tem[1],tem[2]+1) not in visit:
                    heappush(heap, (nums1[tem[1]] + nums2[tem[2]+1], tem[1], tem[2]+1))
                    visit.append((tem[1],tem[2]+1))
            return ret
            
        
        
        
        # return sorted([[i,j] for i in nums1 for j in nums2], key = lambda x:sum(x))[:k]
        