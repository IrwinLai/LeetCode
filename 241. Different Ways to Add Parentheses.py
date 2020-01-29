from functools import lru_cache
class Solution:
    def diffWaysToCompute(self, S: str) -> List[int]:

        def helper(x,y,op):
            return x+y if op == '+' else x*y if op == '*' else x-y
        
        @lru_cache(None)
        def divide(s):
            if s.isdigit():
                return [int(s)]
            res = []
            for i in range(len(s)):
                if s[i] in '+-*':
                    res1 = divide(s[:i])
                    res2 = divide(s[i+1:])
                    for x in res1:
                        for y in res2:
                            res.append(helper(int(x),int(y),s[i]))
            return res
        
        return divide(S)
            