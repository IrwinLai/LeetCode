class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sorted([i*i for i in nums1])
        s2 = sorted([i*i for i in nums2])
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)
        
        count = 0
        n1,n2 = len(s1),len(s2)
        for i in range(n1-1):
            for j in range(i+1,n1):
                tem = nums1[i]*nums1[j]
                if tem > s2[-1]:
                    continue
                elif tem in s2:
                    count += d2[nums1[i]*nums1[j]]
        
        for i in range(n2-1):
            for j in range(i+1,n2):
                tem = nums2[i]*nums2[j]
                if tem > s1[-1]:
                    continue
                elif tem in s1:
                    count += d1[nums2[i]*nums2[j]]
                    
        return count