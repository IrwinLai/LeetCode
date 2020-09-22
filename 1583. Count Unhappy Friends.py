class Solution:
    def unhappyFriends(self, n: int, p: List[List[int]], pairs: List[List[int]]) -> int:
        ans = 0
        d = {}
        for a,b in pairs:
            d[a] = b
            d[b] = a
        for a in d:
            f = 0
            b = d[a]
            for i in p[a]:
                if i == b:
                    break
                # a-i-..-b and i-..-a-..-b
                if p[i].index(a) < p[i].index(d[i]):
                    f = 1
                    break
            ans += f
        return ans
            