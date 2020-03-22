class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        ans = []
        for i in range(len(nums)):
            tem = ans
            ans = tem[:index[i]]
            ans.append(nums[i])
            ans.extend(tem[index[i]:])
        return ans