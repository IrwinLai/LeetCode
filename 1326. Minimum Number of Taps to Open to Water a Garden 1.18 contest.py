class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        effect = []
        for i in range(n+1):
            if ranges[i] != 0:
                effect.append(i)
        tem = [[] for i in range(n+1)]
        for i in effect:
            tem[i] = [i-ranges[i],i+ranges[i]]
        l = 0
        r = 0
        count = 0
        while l < n:
            for i in effect:
                if l >= tem[i][0]:
                    r = max(r,tem[i][1])
            if l == r:
                return -1
            l = r
            count += 1
        return count