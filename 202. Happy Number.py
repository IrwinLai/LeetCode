class Solution:
    def isHappy(self, n: int) -> bool:
        n = sum(map(lambda x:int(x)*int(x),list(str(n))))
        if n == 1:
            return True
        d = []
        while True:
            if n == 1:
                return True
            if n in d:
                return False
            d.append(n)
            n = sum(map(lambda x:int(x)*int(x),list(str(n))))
        