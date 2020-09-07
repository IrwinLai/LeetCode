class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        for i in range(n):
            if i == 0 and s[i] == '?':
                if i+1 < n and s[i+1]=='a':
                    s = 'b'+s[i+1:]
                else:
                    s = 'a'+s[i+1:]
            elif i == n-1 and s[i] == '?':
                if s[i-1]=='a':
                    s = s[:i]+'b'
                else:
                    s = s[:i]+'a'
            elif s[i] == '?':
                for k in range(26):
                    if chr(ord('a')+k) != s[i-1] and chr(ord('a')+k) != s[i+1]:
                        s = s[:i]+ chr(ord('a')+k) + s[i+1:]
                        break
            
        return s