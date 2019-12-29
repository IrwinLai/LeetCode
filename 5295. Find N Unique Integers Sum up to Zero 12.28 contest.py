class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        if n % 2 == 0:
            for i in range(1,n//2+1):
                ret.append(i)
            for i in range(-n//2,0):
                ret.append(i)
        if n % 2 == 1:
            for i in range(-n//2+1,n//2+1):
                ret.append(i)
        return ret
            