class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        '''
        check = []
        for i in range(2**k):
            check.append('0'*(k-len(bin(i)[2:]))+bin(i)[2:])
        # print(check)
        return all(i in s for i in check)
        '''
        arr = [0]*2**k
        tem = 2**(k-1)
        n = 0
        for i in range(len(s)):
            if i >= k and s[i-k] == '1':
                n -= tem
            n = n*2+int(s[i])
            if i >= k-1:
                arr[n] = 1
        return not 0 in arr