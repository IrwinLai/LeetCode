import numpy as np
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums) * len(nums[0]):
            return nums
        return list(np.array(nums).reshape(r,c))