class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            
            l,r = i+1,n-1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t < 0: l += 1
                elif t > 0: r -= 1
                else:
                    ret.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1  
                    l+=1
                    r-=1

        return ret
            
                        