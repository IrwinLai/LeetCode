class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        d = {}
        s,t = list(s),list(t)
        for i in range(n):
            if s[i] in d:
                s[i] = d[s[i]]
            elif t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]
                s[i] = t[i]
        return s == t
                