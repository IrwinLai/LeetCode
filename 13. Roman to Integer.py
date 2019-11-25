class Solution(object):
    def romanToInt(self, s):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        v = d[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if d[s[i]] < d[s[i+1]]:
                v -= d[s[i]]
            else:
                v += d[s[i]]
        return v
            
        