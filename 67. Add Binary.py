class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return str(bin(int(a,2)+int(b,2)))[2:]
        i,j = len(a)-1, len(b)-1
        carry = 0
        ans = ''
        while i >= 0 or j >= 0:
            if i >=0:
                carry += int(a[i])
                i -= 1
            if j>= 0:
                carry += int(b[j])
                j -= 1
            ans += str(carry%2)
            carry //= 2
        if carry == 1:
            ans += '1'
        return ans[::-1]