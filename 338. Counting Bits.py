class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        
        
        return map(lambda x:bin(x)[2:].count('1'), [i for i in range(num+1)])
    