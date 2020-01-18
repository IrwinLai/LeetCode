class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 == 0:
            aim1 = (m+n) // 2
            aim2 = aim1 - 1
        else:
            aim1 = aim2 = (m+n) // 2
        nums1.extend(nums2)
        nums = sorted(nums1)
        
        return (nums[aim1] + nums[aim2])/2
            