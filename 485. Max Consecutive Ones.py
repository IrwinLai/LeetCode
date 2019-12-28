class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(y) for y in ''.join([str(x) for x in nums]).split('0')])
        '''
        count = 0
        ret = 0
        for i in nums:
            if i == 1:
                count += 1
                ret = max(ret,count)
            else:
                count = 0
        return ret
        '''