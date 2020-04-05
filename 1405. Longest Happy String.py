class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def helper(res,l):
            if len(res) <= 1:
                return True
            if res[-1] == l and res[-2] == l:
                return False
            else:
                return True
            
        res = ""
        tem = [['a',a],['b',b],['c',c]]
        while tem[0][1]+tem[1][1]+tem[2][1]:
            tem.sort(key = lambda x:-x[1])
            if helper(res,tem[0][0]):
                tem[0][1] -= 1
                res += tem[0][0]
            elif tem[1][1] > 0:
                tem[1][1] -= 1
                res += tem[1][0]
            else:
                return res
        return res
                