class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)
        for i in range(len(s)):
            if s[i] != '9':
                s1 = s.replace(s[i],'9')
                break
            if i == n-1:
                s1 = s
        
        if s[0] != '1':
            s2 = s.replace(s[0],'1')
        elif n>=2:
            for i in range(1,len(s)):
                if s[i] == s[0]:
                    if s[i] != '1':
                        s2 = s.replace(s[i],'1')
                        break
                if s[i] != s[0]:
                    if s[i] != '0':
                        s2 = s.replace(s[i],'0')
                        break
                if i == n-1:
                    s2 = s
                
        return int(s1) - int(s2)