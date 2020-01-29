class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid
        return min(nums[left],nums[right])