class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        if nums == []:
            return [-1,-1]
        
        l,r = 0, len(nums)-1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] >= t:
                r = m
            else:
                l = m + 1   # move one step every time, make sure to find left bound
                
        if nums[l] != t:
            return [-1,-1]
        ans1 = l
        
        r = len(nums)-1
        while l < r:
            m = l + (r-l) // 2 + 1
            if nums[m] <= t:
                l = m
            else:
                r = m - 1 
        
        return [ans1,r]
            
                
        '''
        nums.append(target)
        a = nums.index(target)
        if a == len(nums)-1:
            return [-1,-1]
        else:
            return [a, a+nums.count(target)-2]
        '''