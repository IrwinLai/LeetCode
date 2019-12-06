class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d1 = collections.Counter(S)
        count = 0
        for i in J:
            count += d1.get(i,0)
        return count