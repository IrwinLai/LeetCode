class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        i = 0
        while True:
            a,b,c = s[i:].find('a'),s[i:].find('b'),s[i:].find('c')
            tem = min(a,b,c) 
            if tem == -1:
                return count
            count += n - i - max(a,b,c)
            i = i+tem+1
        return count