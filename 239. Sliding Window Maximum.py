class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        if n <= k:
            return [max(nums)]
        
        deq = deque()
        res = []
        # find the first max before kth index
        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)
        
        for i in range(k,n):
            res.append(nums[deq[0]])
            
            if deq[0] < i-k+1:
                deq.popleft()
            
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)
        
        res.append(nums[deq[0]])
        
        return res
        
        
                
        
        '''
        # this deque is query anyway, lol
        deque = nums[:k-1]
        res = []
        for i in range(k-1,n):
            deque.append(nums[i])
            res.append(max(deque))
            deque.pop(0)
        return res
        '''