class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        s = list(S)
        def f(s,t,i):
            if i == len(s):  # len is the max index + 1
                res.append(t)
                return 0
            if s[i].isalpha():
                f(s,t+s[i].upper(),i+1)
                f(s,t+s[i].lower(),i+1)
            else:
                f(s,t+s[i],i+1)
            return res
        res = f(s,"",0)
        return res