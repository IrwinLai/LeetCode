class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        tem = 1
        for i in range(n):
            res.append(tem)
            tem*=nums[i]
        tem = 1
        for i in range(n-1,-1,-1):
            res[i]*=tem
            tem*=nums[i]
        return res