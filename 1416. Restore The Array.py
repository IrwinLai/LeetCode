class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            tem = 0
            for i in range(1,len(s)+1):
                if int(s[index:index+i]) > k or i+index > len(s):
                    break
                tem += dp(index+i)
            return tem%(10**9 + 7)
        
        for i in range(len(s))[::-1]:
            res = dp(i)
        return res
                        