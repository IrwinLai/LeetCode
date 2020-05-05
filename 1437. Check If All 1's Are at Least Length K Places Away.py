class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        m = k
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif i == 0 and nums[i] == 1:
                count = 0
            else:
                m = min(count,m)
                if m < k:
                    return False
                count = 0
        return True