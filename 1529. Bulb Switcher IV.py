class Solution:
    def minFlips(self, target: str) -> int:
        if target[0] == '1':
            count = 1
        else:
            count = 0
        for i in range(1,len(target)):
            if target[i] != target[i-1]:
                count += 1
        return count