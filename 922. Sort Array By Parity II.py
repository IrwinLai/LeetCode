class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0] * len(A)
        m = 0
        n = 1
        for i in A:
            if i%2==0:
                res[m] = i
                m += 2
            else:
                res[n] = i
                n += 2
        return res