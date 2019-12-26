class Solution:
    def binaryGap(self, N: int) -> int:
        N = list(str(bin(N))[2:])
        if N.count('1') <= 1:
            return 0
        count = 0
        i = 0
        for j in range(len(N)):
            if N[j] == '1':
                count = max(count,j-i)
                i = j
        return count
            