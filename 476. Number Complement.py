class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join(list(map(lambda x:'0' if x=='1' else '1',list(str(bin(num))[2:])))),2)