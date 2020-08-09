class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def invert(s):
            s = list(s)
            for i in range(len(s)):
                if s[i] == "0":
                    s[i] = "1"
                else:
                    s[i] = "0"
            return "".join(s)
                    
        s = "0"
        for i in range(n):
            s = s + "1" + invert(s)[::-1]
  
        return s[k-1]