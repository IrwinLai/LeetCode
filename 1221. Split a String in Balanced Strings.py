class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        count = 0
        tem = 0
        for j in range(len(s)):
            if s[j] == 'R':
                tem += 1
            elif s[j] == 'L':
                tem -= 1
            if tem == 0:
                i = j+1
                count += 1
        return count