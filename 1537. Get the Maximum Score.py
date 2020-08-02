class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        ind1 = {}
        ind2 = {}
        i = 0
        j = 0
        while i != len(nums1) and j != len(nums2):
            if nums1[i] == nums2[j]:
                ind1[nums1[i]] = i
                ind2[nums2[j]] = j
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1

        @lru_cache(None)
        def dp(i,j):
            if i == 1:
                if j >= len(nums1):
                    return 0
                elif nums1[j] in ind1:
                    return max(dp(2,ind2[nums1[j]]+1)+nums1[j], dp(1,j+1)+nums1[j])
                elif j == len(nums1)-1:
                    return nums1[j]
                else:
                    return dp(1,j+1) +nums1[j]
            else:
                if j >= len(nums2):
                    return 0
                elif nums2[j] in ind2:
                    return max(dp(1,ind1[nums2[j]]+1)+nums2[j], dp(2,j+1)+nums2[j])
                elif j == len(nums2)-1:
                    return nums2[j]
                else:
                    return dp(2,j+1)+nums2[j]
            
        for i in range(len(nums1)-2,100,-100):
            dp(1,i)
        for j in range(len(nums2)-2,100,-100):
            dp(2,j)
                
        res = max(dp(1,0),dp(2,0)) 
        return res% (10**9+7)