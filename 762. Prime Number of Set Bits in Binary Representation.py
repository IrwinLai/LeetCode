class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def isprime(x):
            if x == 0 or x== 1:
                return 0
            if x == 2:
                return 1
            for i in range(2,x//2+2):
                if x % i == 0:
                    return 0
            return 1
        
        p = 0
        for i in range(L,R+1):
            count = 0
            for j in list(str(bin(i))[2:]):
                if j == '1':
                    count += 1
            p += isprime(count)
        return p