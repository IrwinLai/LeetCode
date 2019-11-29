class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        d = {}
        d[0] = 1
        d[1] = 1
        if n >= 2:
            for i in range(2, n+1):
                d[i] = 1.0/i + (i-2)*1.0/i*d[i-1]
        return d[n]