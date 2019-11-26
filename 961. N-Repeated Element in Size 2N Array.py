class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in A:
            if A.count(i) == len(A)/2:
                return i
        return 0