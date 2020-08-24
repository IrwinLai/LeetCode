class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)[::-1]
        ret = ""
        for i in range(3,len(s)+3,3):
            if len(ret) == 0:
                ret = s[0:3]
            else:
                ret +=("."+s[i-3:i])
        return ret[::-1]