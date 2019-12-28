class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 !=0:
            return False
        a = int(sum(A)/3)
        count = 0
        tem = 0
        for i in A:
            tem += i
            if tem == a:
                count += 1
                tem = 0
        return count == 3