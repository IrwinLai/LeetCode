class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)
        for i in d:
            if d[i] == 1:
                return s.index(i)
        return -1