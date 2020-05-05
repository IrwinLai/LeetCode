class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while i < n:
            ma,mi = nums[i],nums[i]
            mai,mii = i,i
            if n - i <= ans:
                return ans
            for j in range(i,n):
                if ma < nums[j]:
                    ma = nums[j]
                    mai = j
                if mi > nums[j]:
                    mi = nums[j]
                    mii = j
                if ma-mi <= limit:
                    ans = max(ans,j-i+1)
                else:
                    i = min(mai,mii) + 1
                    break
            else:
                break
        return ans