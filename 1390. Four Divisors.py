class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
                div = set()
                for j in range(1,int(sqrt(i))+1):
                    if len(div) > 5:
                        div = set()
                        break
                    if i%j == 0:
                        div.add(j)
                        div.add(i//j)
                if len(div) == 4:
                    s += sum(list(div))
        return s