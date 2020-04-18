class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        d = {0:-1}
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count not in d:
                d[count] = i
            else:
                ans = max(ans,i-d[count])
        return ans