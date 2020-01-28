class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        nums2 = nums.copy()
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                nums[i] = nums[i-1]
                nums2[i-1] = nums2[i]
                return nums == sorted(nums) or nums2 == sorted(nums2)
        return True
