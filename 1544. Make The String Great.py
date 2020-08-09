class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        count = 0
        for i in s:
            if i == upper(i):
                count += 1
        for c in range(count):
            for i in range(len(s)-1):
                if s[i] != s[i+1] and (s[i] == upper(s[i+1]) or s[i] == lower(s[i+1])):
                    s = s[:i]+s[i+2:]
                    break
        return "".join(s)