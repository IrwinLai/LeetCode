class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        t = []
        for i in range(n):
            t.append(start + 2*i)

        ans = t[0]
        for i in t[1:][::-1]:
            ans ^= i
        return ans