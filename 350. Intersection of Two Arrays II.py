class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        return list((d1 & d2).elements())