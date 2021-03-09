class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        t1 = t2 = float('inf')
        for n in nums:
            if n <= t1:
                t1 = n
            elif n <= t2:
                t2 = n
            else:
                return True
        return False