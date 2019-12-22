class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = map(lambda x:len(str(x)), nums)
        count = 0
        for i in l:
            if i % 2 == 0:
                count += 1
        return count