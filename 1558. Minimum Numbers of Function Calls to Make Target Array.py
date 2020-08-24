class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while nums != [0]*len(nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    count += 1
            if nums == [0]*len(nums):
                break
            for i in range(len(nums)):
                nums[i] /=2
            count += 1
        return count