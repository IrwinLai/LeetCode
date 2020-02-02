class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        l = []
        count = 1
        for i in range(1,n):
            if s[i] == s[i-1]:
                count += 1
            else:
                l.append(count)
                count = 1
            if i == n-1:
                l.append(count)
        print(l)
        ans = 0
        for i in range(1,len(l)):
            ans += min(l[i-1],l[i])
        return ans
                    
                