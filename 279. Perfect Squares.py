class Solution:
    def numSquares(self, n: int) -> int:
        ps = [i*i for i in range(int(n**0.5)+2)]
        
        count = 0
        level = [n]
        while level:
            tem = []
            count += 1
            for j in level:
                for i in ps:
                    if j == i:
                        return count
                    if j > i:
                        tem.append(j-i)
                    else:
                        break
            level = tem
        