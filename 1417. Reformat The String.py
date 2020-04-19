class Solution:
    def reformat(self, s: str) -> str:
        n = []
        l = []
        for i in s:
            if ord(i) - ord('0') <= 10:
                l.append(i)
            else:
                n.append(i)
        if abs(len(l)-len(n))>1:
            return ""
        ans = ""
        if len(l) <= len(n):
            for i in range(len(l)):
                ans += n[i]
                ans += l[i]
            if len(l) < len(n):  
                ans += n[-1]
        else:
            for i in range(len(n)):
                ans += l[i]
                ans += n[i]
            ans += l[-1]             
        return ans