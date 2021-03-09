class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2 = len(nums1),len(nums2)
        if n1 > 6*n2 or n2 > 6*n1:
            return -1
        
        nums1.sort()
        nums2.sort()
        s1,s2 = sum(nums1),sum(nums2)
        if s1 > s2: 
            return self.minOperations(nums2, nums1) 
        ans = 0
        i,j = 0, n2-1
        print(nums1,nums2,s1,s2)
        while s2 > s1:
            if j < 0 or (i < n1 and 6 - nums1[i] > nums2[j] - 1):
                s1 += 6 - nums1[i]
                i += 1
            else:
                s2 -= nums2[j] - 1    
                j -= 1
            ans += 1
                        
        return ans
        