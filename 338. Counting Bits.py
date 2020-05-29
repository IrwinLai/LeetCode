class Solution:
    def countBits(self, num: int) -> List[int]:
        #return map(lambda x:bin(x)[2:].count('1'), [i for i in range(num+1)])
        
        # 0,1,1,2 / 1,2,2,3 / 1,2,2,3 / 2,3,3,4 / ```
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        return res[:num+1]