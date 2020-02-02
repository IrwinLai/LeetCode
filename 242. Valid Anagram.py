class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = collections.Counter(s)
        d2 = collections.Counter(t)
        for i in list(d1.keys()):
            if d1[i] != d2.get(i,0):
                return False
        return True